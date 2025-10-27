import logging
import json
from pathlib import Path
from pocketflow import Node
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional, Dict, Any
from tqdm import tqdm

from src.utils.data_retrieval import load_all_data
from src.utils.gdsc_utils import chat_with_persona, sanity_check
from src.utils.call_llm import call_llm
from src.utils.matching_rules import EDUCATION_LEVELS, apply_hard_filters, get_required_trainings

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- Pydantic Data Models ---
class PersonaProfile(BaseModel):
    age: int = Field(..., description="The persona's age in years.")
    city: str = Field(..., description="The primary city where the persona lives.")
    education_level: str = Field(..., description="The highest level of education achieved, e.g., 'Ensino Fundamental'.")
    experience_years: int = Field(..., description="Estimated years of professional experience.")
    skills: List[str] = Field(..., description="A list of key skills the persona mentioned.")
    goals: str = Field(..., description="A summary of the persona's career goals or immediate intentions.")
    is_open_to_relocate: bool = Field(..., description="Whether the persona is willing to relocate for a job.")
    languages: List[str] = Field(default=["Portuguese"], description="List of languages the persona speaks.")

class JobProfile(BaseModel):
    job_id: str = Field(..., description="The unique identifier for the job (e.g., 'j10').")
    title: str = Field(..., description="The job title.")
    city: str = Field(..., description="The city where the job is located.")
    is_remote: bool = Field(..., description="Whether the job can be done remotely.")
    education_level: str = Field(..., description="The minimum education level required.")
    experience_years: int = Field(..., description="The minimum years of experience required.")
    languages: List[str] = Field(..., description="List of required languages.")
    required_skills: List[str] = Field(..., description="List of essential skills for the job.")
    
class TrainingProfile(BaseModel):
    training_id: str = Field(..., description="The unique identifier for the training (e.g., 'tr15').")
    title: str = Field(..., description="The title of the training program.")
    offered_skills: List[str] = Field(..., description="A list of skills this training provides.")
    required_level: Optional[str] = Field(None, description="The prerequisite skill level or education, if any.")

# --- Nodes ---
class LoadStaticDataNode(Node):
    # (unchanged)
    def prep(self, shared):
        return None
    def exec(self, prep_res):
        logger.info("Loading all static data (jobs and trainings)...")
        jobs = load_all_data("jobs")
        trainings = load_all_data("trainings")
        return {"jobs": jobs, "trainings": trainings}
    def post(self, shared, prep_res, exec_res):
        shared["all_jobs"] = exec_res.get("jobs", [])
        shared["all_trainings"] = exec_res.get("trainings", [])
        logger.info(f"Loaded {len(shared['all_jobs'])} jobs and {len(shared['all_trainings'])} trainings into shared store.")

class ParseStaticDataNode(Node):
    """
    CORRECTED: Parses raw job and training markdown files into structured Pydantic objects.
    """
    # CORRECTED: The prep method now correctly fetches the raw data from the shared store.
    def prep(self, shared):
        return {
            "raw_jobs": shared.get("all_jobs", []),
            "raw_trainings": shared.get("all_trainings", [])
        }
        
    def _get_cache_path(self, name: str) -> Path:
        return Path("data") / f"parsed_{name}.json"
        
    def _load_from_cache(self, name: str, model: BaseModel) -> Optional[List[BaseModel]]:
        cache_path = self._get_cache_path(name)
        if cache_path.exists():
            logger.info(f"Loading parsed {name} from cache: {cache_path}")
            with open(cache_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [model.model_validate(item) for item in data]
        return None

    def _save_to_cache(self, name: str, data: List[BaseModel]):
        cache_path = self._get_cache_path(name)
        logger.info(f"Saving {len(data)} parsed {name} to cache: {cache_path}")
        dict_data = [item.model_dump() for item in data]
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, indent=2, ensure_ascii=False)

    def _parse_item(self, item: Dict[str, str], schema: Dict, item_id_key: str) -> Optional[Dict[str, Any]]:
        # (unchanged)
        item_id = item.get("id")
        content = item.get("content")
        prompt = f"""
        Analyze the following document and extract its properties into a valid JSON object that strictly follows this schema.
        The '{item_id_key}' must be set to '{item_id}'.
        JSON Schema:
        ---
        {json.dumps(schema, indent=2)}
        ---
        Document:
        ---
        {content}
        ---
        Respond ONLY with the JSON object.
        """
        try:
            response_str = call_llm(prompt=prompt, use_cache=True, model="mistral-small-latest")
            cleaned_str = response_str.strip().replace("```json", "").replace("```", "")
            return json.loads(cleaned_str)
        except (json.JSONDecodeError, Exception) as e:
            logger.error(f"Failed to parse item {item_id}: {e}")
            return None

    # CORRECTED: The exec method now receives the raw data from prep_res.
    def exec(self, prep_res: Dict):
        raw_jobs = prep_res["raw_jobs"]
        raw_trainings = prep_res["raw_trainings"]
        
        parsed_jobs = self._load_from_cache("jobs", JobProfile)
        if not parsed_jobs:
            logger.info("Job cache not found. Parsing all jobs from markdown...")
            job_schema = JobProfile.model_json_schema()
            parsed_job_data = [
                self._parse_item(job, job_schema, "job_id") 
                for job in tqdm(raw_jobs, desc="Parsing Jobs")
            ]
            parsed_jobs = [JobProfile.model_validate(data) for data in parsed_job_data if data]
            self._save_to_cache("jobs", parsed_jobs)

        parsed_trainings = self._load_from_cache("trainings", TrainingProfile)
        if not parsed_trainings:
            logger.info("Training cache not found. Parsing all trainings from markdown...")
            training_schema = TrainingProfile.model_json_schema()
            parsed_training_data = [
                self._parse_item(training, training_schema, "training_id") 
                for training in tqdm(raw_trainings, desc="Parsing Trainings")
            ]
            parsed_trainings = [TrainingProfile.model_validate(data) for data in parsed_training_data if data]
            self._save_to_cache("trainings", parsed_trainings)
            
        return {"parsed_jobs": parsed_jobs, "parsed_trainings": parsed_trainings}
        
    def post(self, shared, prep_res, exec_res):
        # (unchanged)
        shared["parsed_jobs"] = exec_res.get("parsed_jobs", [])
        shared["parsed_trainings"] = exec_res.get("parsed_trainings", [])
        logger.info(f"Loaded {len(shared['parsed_jobs'])} parsed jobs and {len(shared['parsed_trainings'])} parsed trainings into shared store.")

class ExtractProfileNode(Node):
    def prep(self, shared):
        persona_id = shared.get("persona_id")
        if not persona_id:
            raise ValueError("persona_id not found in shared store.")
        return {"persona_id": persona_id}

    def exec(self, prep_res):
        persona_id = prep_res["persona_id"]
        logger.info(f"Starting DYNAMIC conversation with {persona_id}...")
        
        conversation_id = None
        conversation_history = []
        persona_profile = {}
        
        # --- Conversation Loop Constants ---
        MAX_TURNS = 8
        MIN_TURNS = 5

        for turn in range(MAX_TURNS):
            logger.info(f"Conversation Turn {turn + 1}/{MAX_TURNS}")
            
            # 1. Analyze current history to extract whatever profile data is available
            schema = PersonaProfile.model_json_schema()
            transcript = "\n".join([f"Q: {entry['question']}\nA: {entry['answer']}" for entry in conversation_history])
            
            current_profile_data = {}
            if transcript:
                analysis_prompt = f"""
                Analyze the conversation transcript and extract the user's profile into a valid JSON object that strictly follows this schema.
                If a value is not mentioned, omit the key.

                JSON Schema:
                ---
                {json.dumps(schema, indent=2)}
                ---
                Conversation Transcript:
                ---
                {transcript}
                ---
                Respond ONLY with the JSON object.
                """
                profile_str = call_llm(prompt=analysis_prompt, use_cache=False)
                try:
                    cleaned_str = profile_str.strip().replace("```json", "").replace("```", "")
                    current_profile_data = json.loads(cleaned_str)
                except (json.JSONDecodeError, Exception) as e:
                    logger.warning(f"Could not parse partial profile on turn {turn+1}: {e}. Continuing conversation.")
            
            # 2. Check for completion ONLY after minimum turns
            is_complete = False
            missing_fields = []
            try:
                PersonaProfile.model_validate(current_profile_data)
                is_complete = True
            except ValidationError as e:
                missing_fields = [err['loc'][0] for err in e.errors()]
            
            # MODIFIED LOGIC: Break only if the profile is complete AND min turns are met
            if is_complete and (turn + 1) >= MIN_TURNS:
                logger.info(f"Profile is complete after {turn + 1} turns. Ending conversation.")
                persona_profile = current_profile_data
                break
            else:
                 logger.info(f"Profile is not yet complete. Missing fields: {missing_fields if not is_complete else 'N/A (min turns not met)'}")


            # 3. Generate the next question
            if turn == 0:
                next_question = "Hello! To help you find the right green job opportunities, could you please tell me a bit about yourself? For example, your age, languages and current city in Brazil."
            else:
                next_question_prompt = f"""
                You are an expert career advisor conducting a friendly interview. Based on the conversation so far, you need to ask a question to gather the following missing information: {', '.join(missing_fields)}.
                
                - Ask only ONE clear and concise question.
                - Phrase the question naturally based on the last answer.
                - Do not repeat questions that have already been answered.

                Conversation History:
                ---
                {transcript}
                ---

                What is the next best question to ask? Respond ONLY with the question text.
                """
                next_question = call_llm(prompt=next_question_prompt, use_cache=False)

            # 4. Interact with the persona
            logger.info(f"Asking: {next_question}")
            response_tuple = chat_with_persona(
                persona_id=persona_id, message=next_question, conversation_id=conversation_id
            )
            if response_tuple is None:
                raise RuntimeError("The chat_with_persona API call failed.")
            response, conversation_id = response_tuple
            logger.info(f"Response: {response}")
            conversation_history.append({"question": next_question, "answer": response})

            if turn == MAX_TURNS - 1:
                logger.warning(f"Max conversation turns ({MAX_TURNS}) reached. Proceeding with collected data.")
                persona_profile = current_profile_data

        # --- Final Validation ---
        try:
            final_profile = PersonaProfile.model_validate(persona_profile)
        except ValidationError as e:
            logger.error(f"Conversation ended, but profile is still incomplete. Raw data: {persona_profile}")
            raise RuntimeError(f"Could not build a complete persona profile. Validation errors: {e}")

        return {
            "persona_profile": final_profile,
            "conversation_id": conversation_id,
            "conversation_history": conversation_history
        }
    
    def post(self, shared, prep_res, exec_res):
        shared["persona_profile"] = exec_res["persona_profile"]
        shared["conversation_id"] = exec_res["conversation_id"]
        shared["conversation_history"] = exec_res["conversation_history"]
        logger.info(f"Successfully extracted and validated profile for {shared['persona_id']}.")
        
class DecisionNode(Node):
    def prep(self, shared):
        profile = shared.get("persona_profile")
        if not profile or not isinstance(profile, PersonaProfile):
            raise ValueError("A valid PersonaProfile object was not found in the shared store.")
        return profile
    def exec(self, profile: PersonaProfile) -> str:
        logger.info(f"Making decision for persona with age {profile.age} and goals: '{profile.goals}'")
        if profile.age < 16:
            logger.info("Decision: provide_awareness_young (age < 16)")
            return "provide_awareness_young"
        informational_keywords = ["exploring", "explorar", "curious", "curioso", "just looking", "só olhando", "not sure", "não sei"]
        if any(keyword in profile.goals.lower() for keyword in informational_keywords):
            logger.info("Decision: provide_awareness_info (informational goals)")
            return "provide_awareness_info"
        training_keywords = ["training", "treinamento", "courses", "cursos", "learn", "aprender", "study", "estudar", "upskill"]
        job_keywords = ["job", "emprego", "work", "trabalhar", "career", "carreira"]
        has_training_goal = any(keyword in profile.goals.lower() for keyword in training_keywords)
        has_job_goal = any(keyword in profile.goals.lower() for keyword in job_keywords)
        if has_training_goal and not has_job_goal:
            logger.info("Decision: recommend_trainings (training-focused goals)")
            return "recommend_trainings"
        logger.info("Decision: recommend_jobs (default path)")
        return "recommend_jobs"
    def post(self, shared, prep_res, exec_res: str) -> Optional[str]:
        shared["decision_action"] = exec_res
        logger.info(f"Decision action '{exec_res}' stored in shared store.")
        
        return exec_res
        
class ProvideAwarenessNode(Node):
    def prep(self, shared):
        decision = shared.get("decision_action")
        if not decision or "provide_awareness" not in decision:
            raise ValueError(f"Invalid decision action '{decision}' for ProvideAwarenessNode.")
        return decision
    def exec(self, decision: str) -> Dict[str, Any]:
        if decision == "provide_awareness_young":
            reason = "too_young"
            logger.info("Formatting awareness response for reason: too_young.")
        else:
            reason = "info"
            logger.info("Formatting awareness response for reason: info.")
        return {
            "predicted_type": "awareness",
            "predicted_items": reason
        }
    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        logger.info(f"Awareness recommendation stored in 'intermediate_recommendations'.")

class FindTrainingsOnlyNode(Node):
    """
    Finds and recommends the immediate next-level trainings for a persona.
    Now includes trainings with no prerequisites as valid options.
    """
    def prep(self, shared):
        profile = shared.get("persona_profile")
        trainings = shared.get("parsed_trainings")
        if not profile or not trainings:
            raise ValueError("Persona profile or parsed trainings not found in shared store.")
        return {"profile": profile, "trainings": trainings}

    def exec(self, prep_res: Dict) -> Dict[str, Any]:
        profile: PersonaProfile = prep_res["profile"]
        all_trainings: List[TrainingProfile] = prep_res["trainings"]
        
        persona_edu_level_num = EDUCATION_LEVELS.get(profile.education_level, 0)
        logger.info(f"Persona education level: '{profile.education_level}' (Numeric: {persona_edu_level_num}).")

        recommended_trainings = []
        for training in all_trainings:
            training_req_level_num = EDUCATION_LEVELS.get(training.required_level, 0)
            
            # --- IMPROVED LOGIC ---
            # Recommend trainings that are one level higher OR have no level requirement (are open to all)
            if (training_req_level_num == persona_edu_level_num + 1) or (training_req_level_num == 0):
                recommended_trainings.append({"training_id": training.training_id})
        
        logger.info(f"Found {len(recommended_trainings)} trainings (next-level or open-to-all).")
        
        return {
            "predicted_type": "trainings_only",
            "trainings": recommended_trainings
        }

    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        logger.info("Training-only recommendation stored in 'intermediate_recommendations'.")
        
class FindJobsAndTrainingsNode(Node):
    """
    Finds suitable jobs using a hybrid approach:
    1. Fast, rule-based hard filters to find all technically eligible jobs.
    2. An LLM-based "soft filter" to score the relevance of eligible jobs.
    3. Recommends trainings for skill gaps on only the top-scoring jobs.
    """
    def prep(self, shared):
        profile = shared.get("persona_profile")
        jobs = shared.get("parsed_jobs")
        trainings = shared.get("parsed_trainings")
        if not all([profile, jobs, trainings]):
            raise ValueError("Persona profile, parsed jobs, or parsed trainings not found.")
        return {"profile": profile, "jobs": jobs, "trainings": trainings}

    def _get_relevance_score(self, persona: PersonaProfile, job: JobProfile, use_cache: bool = True, model: str = "mistral-small-latest") -> int:
        """Calls an LLM to score the relevance of a job to a persona."""
        # --- NEW, MORE ROBUST PROMPT ---
        prompt = f"""
        You are an expert career advisor in Brazil. Your task is to score the relevance of a job for a specific persona based on their skills and, most importantly, their stated career goals.

        **Persona Profile:**
        - **Stated Goals:** "{persona.goals}"
        - **Existing Skills:** {persona.skills}

        **Job to Evaluate:**
        - **Title:** "{job.title}"
        - **Required Skills:** {job.required_skills}

        **Scoring Criteria:**
        - **High Score (8-10):** The job title and its domain (e.g., finance, data, sustainability) directly align with the persona's stated goals.
        - **Medium Score (4-7):** The job shares keywords (like 'Analyst') but is in a different domain than the persona's goals (e.g., Design Analyst for a Data Analyst persona).
        - **Low Score (1-3):** The job is in a completely different field.

        On a scale of 1 to 10, how relevant is this job to the persona?

        **CRITICAL INSTRUCTION:** Your response MUST be a single, valid JSON object and nothing else. The 'reasoning' string must NOT contain any newline characters (`\\n`) or other control characters. It must be a single line of text.

        **Example of a valid response:**
        {{"score": 8, "reasoning": "This job is a strong match because the domain aligns with the persona's goals."}}

        Respond now.
        """
        try:
            response_str = call_llm(prompt=prompt, use_cache=use_cache, model=model)
            # Standard cleaning should be sufficient with the improved prompt
            cleaned_str = response_str.strip().replace("```json", "").replace("```", "")
            response_json = json.loads(cleaned_str)
            score = int(response_json.get("score", 0))
            logger.debug(f"Job {job.job_id} ('{job.title}') scored {score} using {model}. Reason: {response_json.get('reasoning')}")
            return score
        except (json.JSONDecodeError, ValueError, Exception) as e:
            logger.warning(f"Could not parse relevance score for job {job.job_id} using {model}. Error: {e}. Raw response: '{response_str}'")
            return 0

    def exec(self, prep_res: Dict) -> Dict[str, Any]:
        profile: PersonaProfile = prep_res["profile"]
        all_jobs: List[JobProfile] = prep_res["jobs"]
        all_trainings: List[TrainingProfile] = prep_res["trainings"]

        # Get parameters from the node instance
        use_cache_for_scoring = self.params.get("use_cache_for_scoring", True)
        scoring_model = self.params.get("scoring_model", "mistral-small-latest")
        logger.info(f"Using model '{scoring_model}' for relevance scoring.")

        profile_dict = profile.model_dump()

        candidate_jobs = [
            job for job in all_jobs 
            if apply_hard_filters(profile_dict, job.model_dump())
        ]
        logger.info(f"Found {len(candidate_jobs)} candidate jobs after applying hard filters.")

        if not candidate_jobs:
            return {"predicted_type": "jobs+trainings", "jobs": []}

        scored_jobs = []
        for job in tqdm(candidate_jobs, desc=f"Scoring jobs with {scoring_model}", disable=len(candidate_jobs) < 5):
            score = self._get_relevance_score(profile, job, use_cache=use_cache_for_scoring, model=scoring_model)
            scored_jobs.append({"job": job, "score": score})

        sorted_jobs = sorted(scored_jobs, key=lambda x: x["score"], reverse=True)
        
        top_jobs = [item["job"] for item in sorted_jobs[:3]]
        logger.info(f"Selected top {len(top_jobs)} jobs after relevance scoring.")

        job_recommendations = []
        for job in top_jobs:
            job_dict = job.model_dump()
            missing_skills = get_required_trainings(profile_dict, job_dict)
            
            suggested_trainings = []
            if missing_skills:
                for skill in missing_skills:
                    matching_trainings = [
                        {"training_id": t.training_id}
                        for t in all_trainings
                        if skill.lower() in [s.lower() for s in t.offered_skills]
                    ]
                    if matching_trainings:
                        suggested_trainings.append({
                            "missing_skill": skill,
                            "trainings": matching_trainings
                        })
            
            job_recommendations.append({
                "job_id": job.job_id,
                "suggested_trainings": suggested_trainings
            })

        return {
            "predicted_type": "jobs+trainings",
            "jobs": job_recommendations
        }
        
    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        logger.info("Jobs+trainings recommendation stored in 'intermediate_recommendations'.")
        
class FinalizeOutputNode(Node):
    def prep(self, shared):
        persona_id = shared.get("persona_id")
        recs = shared.get("intermediate_recommendations")
        if not persona_id or not recs:
            raise ValueError("Persona ID or intermediate recommendations not found in shared store.")
        return {"persona_id": persona_id, "recommendations": recs}
    def exec(self, prep_res: Dict) -> Dict[str, Any]:
        final_output = {
            "persona_id": prep_res["persona_id"],
            **prep_res["recommendations"]
        }
        logger.info(f"Final output formatted for persona {prep_res['persona_id']}.")
        return final_output
    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["final_recommendation"] = exec_res
        logger.info("Final recommendation stored in shared store.")