import logging
import json
from pathlib import Path
from pocketflow import Node
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional, Dict, Any
from tqdm import tqdm

from src.utils.data_retrieval import load_all_data
from src.utils.gdsc_utils import chat_with_persona
from src.utils.call_llm import call_llm
# MODIFIED: Import the new scoring functions
from src.utils.matching_rules import (
    get_required_trainings,
    safety_net_filter,
    calculate_composite_score,
    calculate_training_composite_score,
    keyword_relevance_filter
)

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- Pydantic Data Models (Unchanged) ---
class PersonaProfile(BaseModel):
    persona_id: str = Field(..., description="The persona's unique identifier.")
    age: int = Field(..., description="The persona's age in years.")
    city: Optional[str] = Field(None, description="The city where the job is located, if specified.")
    education_level: str = Field(..., description="The highest level of education achieved, e.g., 'Ensino Fundamental'.")
    experience_years: int = Field(..., description="Estimated years of professional experience.")
    skills: List[str] = Field(..., description="A list of key skills the persona mentioned.")
    goals: str = Field(..., description="A summary of the persona's career goals or immediate intentions.")
    is_open_to_relocate: bool = Field(..., description="Whether the persona is willing to relocate for a job.")
    languages: List[str] = Field(default=["Portuguese"], description="List of languages the persona speaks.")

class JobProfile(BaseModel):
    job_id: str = Field(..., description="The unique identifier for the job (e.g., 'j10').")
    title: str = Field(..., description="The job title.")
    city: Optional[str] = Field(None, description="The city where the job is located, if specified.")
    is_remote: bool = Field(default=False, description="Whether the job can be done remotely.")
    education_level: Optional[str] = Field(None, description="The minimum education level required.")
    experience_years: int = Field(default=0, description="The minimum years of experience required.")
    languages: List[str] = Field(default=[], description="List of required languages.")
    required_skills: List[str] = Field(default=[], description="List of essential skills for the job.")
    
class TrainingProfile(BaseModel):
    training_id: str = Field(..., description="The unique identifier for the training (e.g., 'tr15').")
    title: str = Field(..., description="The title of the training program.")
    offered_skills: List[str] = Field(default=[], description="A list of skills this training provides.")
    required_level: Optional[str] = Field(None, description="The prerequisite skill level or education, if any.")


# --- Nodes (Only FindJobsAndTrainingsNode is modified) ---

class LoadStaticDataNode(Node):
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
    def prep(self, shared):
        return {
            "raw_jobs": shared.get("all_jobs", []),
            "raw_trainings": shared.get("all_trainings", [])
        }
    def _get_cache_path(self, name: str, suffix: str = "") -> Path:
        if suffix:
            return Path("data") / f"parsed_{name}{suffix}.json"
        return Path("data") / f"parsed_{name}.json"
    def _load_from_cache(self, name: str, model: BaseModel) -> Optional[List[BaseModel]]:
        suffix = self.params.get("cache_suffix", "")
        cache_path = self._get_cache_path(name, suffix)
        if cache_path.exists():
            logger.info(f"Loading parsed {name} from cache: {cache_path}")
            with open(cache_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [model.model_validate(item) for item in data]
        return None
    def _save_to_cache(self, name: str, data: List[BaseModel]):
        suffix = self.params.get("cache_suffix", "")
        cache_path = self._get_cache_path(name, suffix)
        logger.info(f"Saving {len(data)} parsed {name} to cache: {cache_path}")
        dict_data = [item.model_dump() for item in data]
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, indent=2, ensure_ascii=False)
    def _parse_item(self, item: Dict[str, str], schema: Dict, item_id_key: str) -> Optional[Dict[str, Any]]:
        # This function's internal logic is complex but correct. No changes needed.
        item_id, content = item.get("id"), item.get("content")
        prompt = f"""
        Analyze the document and extract its properties into a JSON object following this schema.
        - The '{item_id_key}' must be '{item_id}'.
        - For 'education_level' or 'required_level', map any prerequisite to an exact value from: ["Ensino Fundamental", "Ensino Médio", "Técnico", "Tecnólogo", "Graduação", "Pós-graduação", "Mestrado", "Doutorado"].
        - Infer the closest formal level (e.g., "Tecnólogo degree" -> "Tecnólogo", "no prerequisites" -> null).
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
            model = self.params.get("parsing_model", "mistral-large-latest")
            resp = call_llm(prompt=prompt, use_cache=True, model=model)
            return json.loads(resp.strip().replace("```json", "").replace("```", ""))
        except Exception as e:
            logger.error(f"Failed to parse item {item_id}: {e}")
            return None
    def exec(self, prep_res: Dict):
        raw_jobs, raw_trainings = prep_res["raw_jobs"], prep_res["raw_trainings"]
        parsed_jobs = self._load_from_cache("jobs", JobProfile)
        if not parsed_jobs:
            schema = JobProfile.model_json_schema()
            data = [self._parse_item(j, schema, "job_id") for j in tqdm(raw_jobs, "Parsing Jobs")]
            parsed_jobs = [JobProfile.model_validate(d) for d in data if d]
            self._save_to_cache("jobs", parsed_jobs)
        parsed_trainings = self._load_from_cache("trainings", TrainingProfile)
        if not parsed_trainings:
            schema = TrainingProfile.model_json_schema()
            data = [self._parse_item(t, schema, "training_id") for t in tqdm(raw_trainings, "Parsing Trainings")]
            parsed_trainings = [TrainingProfile.model_validate(d) for d in data if d]
            self._save_to_cache("trainings", parsed_trainings)
        return {"parsed_jobs": parsed_jobs, "parsed_trainings": parsed_trainings}
    def post(self, shared, prep_res, exec_res):
        shared["parsed_jobs"] = exec_res.get("parsed_jobs", [])
        shared["parsed_trainings"] = exec_res.get("parsed_trainings", [])
        logger.info(f"Loaded {len(shared['parsed_jobs'])} parsed jobs and {len(shared['parsed_trainings'])} parsed trainings.")

class ExtractProfileNode(Node):
    # Unchanged. This node is complex but works as intended.
    def prep(self, shared):
        persona_id = shared.get("persona_id")
        if not persona_id: raise ValueError("persona_id not found")
        return {"persona_id": persona_id}
    def exec(self, prep_res):
        persona_id = prep_res["persona_id"]
        model = self.params.get("interview_model", "mistral-small-latest")
        logger.info(f"Starting DYNAMIC conversation with {persona_id} using {model}...")
        history, profile_data, convo_id = [], {}, None
        MAX_TURNS, MIN_TURNS = 8, 5
        for turn in range(MAX_TURNS):
            transcript = "\n".join([f"Q: {h['question']}\nA: {h['answer']}" for h in history])
            if transcript:
                analysis_prompt = f"Analyze conversation and extract profile into JSON (schema: {json.dumps(PersonaProfile.model_json_schema(), indent=2)}). persona_id must be '{persona_id}'. Omit unmentioned keys. Transcript:\n---\n{transcript}\n---\nRespond ONLY with JSON."
                try:
                    profile_data = json.loads(call_llm(prompt=analysis_prompt, use_cache=False, model=model).strip().replace("```json", "").replace("```", ""))
                except Exception: pass
            is_complete, missing = False, []
            try:
                profile_data['persona_id'] = persona_id
                PersonaProfile.model_validate(profile_data)
                is_complete = True
            except ValidationError as e:
                missing = [err['loc'][0] for err in e.errors() if err['loc'][0] != 'persona_id']
            if is_complete and (turn + 1) >= MIN_TURNS:
                logger.info(f"Profile complete in {turn+1} turns.")
                break
            question = "Hello! Tell me about yourself: age, languages, current city in Brazil." if turn == 0 else call_llm(f"You are a career advisor. Based on history, ask ONE question to gather missing info: {', '.join(missing)}. History:\n---\n{transcript}\n---\nNext question?", use_cache=False, model=model)
            resp, convo_id = chat_with_persona(persona_id, question, convo_id)
            history.append({"question": question, "answer": resp})
            if turn == MAX_TURNS - 1: logger.warning("Max turns reached.")
        final_profile = PersonaProfile.model_validate(profile_data)
        return {"persona_profile": final_profile, "conversation_id": convo_id, "conversation_history": history}
    def post(self, shared, prep_res, exec_res):
        shared.update(exec_res)
        logger.info(f"Successfully extracted profile for {shared['persona_id']}.")

class DecisionNode(Node):
    # Unchanged
    def prep(self, shared):
        profile = shared.get("persona_profile")
        if not profile: raise ValueError("PersonaProfile not found.")
        return profile
    def exec(self, profile: PersonaProfile):
        if profile.age < 16: return "provide_awareness_young"
        info_kw = ["exploring", "curious", "not sure"]
        train_kw = ["training", "courses", "learn", "study"]
        job_kw = ["job", "work", "career"]
        goals = profile.goals.lower()
        if any(kw in goals for kw in info_kw): return "provide_awareness_info"
        if any(kw in goals for kw in train_kw) and not any(kw in goals for kw in job_kw): return "recommend_trainings"
        return "recommend_jobs"
    def post(self, shared, prep_res, exec_res):
        shared["decision_action"] = exec_res
        return exec_res

# class ProvideAwarenessNode(Node):
#     # Unchanged
#     def exec(self, prep_res):
#         reason = "too_young" if shared.get("decision_action") == "provide_awareness_young" else "info"
#         return {"predicted_type": "awareness", "predicted_items": reason}
#     def post(self, shared, prep_res, exec_res):
#         shared["intermediate_recommendations"] = exec_res
        # In src/nodes.py, replace the old ProvideAwarenessNode with this:

class ProvideAwarenessNode(Node):
    def prep(self, shared):
        # CORRECT: Prep method reads from shared and returns the necessary data.
        decision = shared.get("decision_action")
        if not decision or "provide_awareness" not in decision:
            # This check is better placed in prep.
            raise ValueError(f"Invalid decision action '{decision}' for ProvideAwarenessNode.")
        return decision

    def exec(self, decision_action: str) -> Dict[str, Any]:
        # CORRECT: Exec method now receives the decision_action from prep_res.
        # It no longer tries to access the 'shared' dictionary.
        reason = "too_young" if decision_action == "provide_awareness_young" else "info"
        logger.info(f"Formatting awareness response for reason: {reason}.")
        return {
            "predicted_type": "awareness",
            "predicted_items": reason
        }

    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        logger.info(f"Awareness recommendation stored in 'intermediate_recommendations'.")

class FindTrainingsOnlyNode(Node):
    """
    Finds and recommends trainings by applying a graduated scoring model
    to all trainings in the dataset.
    """
    def prep(self, shared):
        profile = shared.get("persona_profile")
        trainings = shared.get("parsed_trainings")
        if not profile or not trainings:
            raise ValueError("Persona profile or parsed trainings not found in shared store.")
        return {"profile": profile, "trainings": trainings}

    # def exec(self, prep_res: Dict) -> Dict[str, Any]:
    #     profile: PersonaProfile = prep_res["profile"]
    #     all_trainings: List[TrainingProfile] = prep_res["trainings"]
        
    #     profile_dict = profile.model_dump()

    #     # Score all 497 trainings. This is feasible because the LLM call is cheap and cached.
    #     scored_trainings = []
    #     for training in tqdm(all_trainings, desc=f"Scoring trainings for persona {profile.persona_id}", disable=len(all_trainings) < 10):
    #         training_dict = training.model_dump()
    #         composite_score, sub_scores = calculate_training_composite_score(profile_dict, training_dict)
    #         scored_trainings.append({"training": training, "score": composite_score, "sub_scores": sub_scores})
            
    #     # Sort and select the top 5 trainings
    #     sorted_trainings = sorted(scored_trainings, key=lambda x: x["score"], reverse=True)
    #     self.ranked_trainings_for_tracing = sorted_trainings
    #     top_trainings_scored = sorted_trainings[:5]

    #     logger.info(f"--- Top 5 Trainings for Persona {profile.persona_id} ---")
    #     for scored_training in top_trainings_scored:
    #         logger.info(
    #             f"  - Training: {scored_training['training'].training_id} ({scored_training['training'].title}) | "
    #             f"Composite Score: {scored_training['score']:.2f} | "
    #             f"Sub-scores: {scored_training['sub_scores']}"
    #         )
            
    #     recommended_trainings = [{"training_id": t["training"].training_id} for t in top_trainings_scored]

    #     return {
    #         "predicted_type": "trainings_only",
    #         "trainings": recommended_trainings
    #     }
    # In class FindTrainingsOnlyNode:
    # def exec(self, prep_res: Dict) -> Dict[str, Any]:
    #     profile: PersonaProfile = prep_res["profile"]
    #     all_trainings: List[TrainingProfile] = prep_res["trainings"]
        
    #     profile_dict = profile.model_dump()
    #     from src.utils.matching_rules import get_education_level, score_training_prerequisite_fit

    #     # --- STAGE 1: Fast, Non-LLM Pre-filter ---
    #     # First, create a list of candidates based only on the cheap prerequisite score.
    #     persona_edu_level = get_education_level(profile.education_level)
        
    #     candidate_trainings = []
    #     for training in all_trainings:
    #         training_req_level = get_education_level(training.required_level)
    #         prereq_score = score_training_prerequisite_fit(persona_edu_level, training_req_level)
            
    #         # We only consider trainings that are a decent prerequisite fit
    #         if prereq_score >= 60: # (60 = overqualified, 100 = perfect/next-level)
    #             candidate_trainings.append({"training": training, "prereq_score": prereq_score})

    #     logger.info(f"Filtered {len(all_trainings)} total trainings down to {len(candidate_trainings)} candidates based on prerequisite fit.")

    #     if not candidate_trainings:
    #         return {"predicted_type": "trainings_only", "trainings": []}

    #     # --- STAGE 2: Expensive LLM Scoring on the smaller candidate list ---
    #     from src.utils.matching_rules import score_training_goal_alignment
        
    #     fully_scored_trainings = []
    #     for item in tqdm(candidate_trainings, desc=f"Scoring training goals for persona {profile.persona_id}", disable=len(candidate_trainings) < 10):
    #         training = item["training"]
    #         goal_score = score_training_goal_alignment(
    #             profile.goals, training.title, training.offered_skills
    #         )
            
    #         # --- STAGE 3: Final Composite Score Calculation ---
    #         # Using the pre-calculated prerequisite score and the new goal score
    #         sub_scores = {
    #             'prerequisite': item["prereq_score"],
    #             'goal_alignment': goal_score
    #         }
    #         weights = {'prerequisite': 0.40, 'goal_alignment': 0.60}
    #         composite_score = round(sum(sub_scores[dim] * weights[dim] for dim in sub_scores), 2)
            
    #         fully_scored_trainings.append({
    #             "training": training,
    #             "score": composite_score,
    #             "sub_scores": sub_scores
    #         })
            
    #     # Sort and select the top 5 trainings
    #     sorted_trainings = sorted(fully_scored_trainings, key=lambda x: x["score"], reverse=True)
    #     self.ranked_trainings_for_tracing = sorted_trainings # For tracing artifact
    #     top_trainings_scored = sorted_trainings[:5]

    #     logger.info(f"--- Top 5 Trainings for Persona {profile.persona_id} ---")
    #     for scored_training in top_trainings_scored:
    #         logger.info(
    #             f"  - Training: {scored_training['training'].training_id} ({scored_training['training'].title}) | "
    #             f"Composite Score: {scored_training['score']:.2f} | "
    #             f"Sub-scores: {scored_training['sub_scores']}"
    #         )
            
    #     recommended_trainings = [{"training_id": t["training"].training_id} for t in top_trainings_scored]

    #     return {
    #         "predicted_type": "trainings_only",
    #         "trainings": recommended_trainings
    #     }
    # In class FindTrainingsOnlyNode:
    def exec(self, prep_res: Dict) -> Dict[str, Any]:
        profile: PersonaProfile = prep_res["profile"]
        all_trainings: List[TrainingProfile] = prep_res["trainings"]
        
        profile_dict = profile.model_dump()
        from src.utils.matching_rules import get_education_level, score_training_prerequisite_fit

        # --- STAGE 1: Fast, Non-LLM Prerequisite Pre-filter ---
        persona_edu_level = get_education_level(profile.education_level)
        stage1_candidates = []
        for training in all_trainings:
            training_req_level = get_education_level(training.required_level)
            prereq_score = score_training_prerequisite_fit(persona_edu_level, training_req_level)
            if prereq_score >= 60:
                stage1_candidates.append({"training": training, "prereq_score": prereq_score})
        logger.info(f"Stage 1: Prerequisite filter reduced {len(all_trainings)} trainings to {len(stage1_candidates)}.")

        # --- STAGE 2: Fast, Non-LLM Keyword Pre-filter ---
        stage2_candidates = [
            item for item in stage1_candidates
            if keyword_relevance_filter(profile_dict, item["training"].model_dump())
        ]
        logger.info(f"Stage 2: Keyword filter reduced candidates to {len(stage2_candidates)}.")
        
        # --- STAGE 3: Hard Cap for Safety ---
        MAX_LLM_CALLS = 50
        if len(stage2_candidates) > MAX_LLM_CALLS:
            # Sort by the cheap prerequisite score to keep the most relevant ones
            stage2_candidates = sorted(stage2_candidates, key=lambda x: x["prereq_score"], reverse=True)[:MAX_LLM_CALLS]
            logger.warning(f"Stage 3: Candidate list capped to {len(stage2_candidates)} to control costs.")
        
        final_candidates = stage2_candidates

        if not final_candidates:
            return {"predicted_type": "trainings_only", "trainings": []}

        # --- STAGE 4: Expensive LLM Scoring on the final, small candidate list ---
        from src.utils.matching_rules import score_training_goal_alignment
        
        fully_scored_trainings = []
        for item in tqdm(final_candidates, desc=f"Scoring final training candidates for {profile.persona_id}", disable=len(final_candidates) < 5):
            training = item["training"]
            goal_score = score_training_goal_alignment(profile.goals, training.title, training.offered_skills)
            sub_scores = {'prerequisite': item["prereq_score"], 'goal_alignment': goal_score}
            weights = {'prerequisite': 0.40, 'goal_alignment': 0.60}
            composite_score = round(sum(sub_scores[dim] * weights[dim] for dim in sub_scores), 2)
            
            fully_scored_trainings.append({"training": training, "score": composite_score, "sub_scores": sub_scores})
            
        sorted_trainings = sorted(fully_scored_trainings, key=lambda x: x["score"], reverse=True)
        self.ranked_trainings_for_tracing = sorted_trainings
        top_trainings_scored = sorted_trainings[:5]
        
        logger.info(f"--- Top 5 Trainings for Persona {profile.persona_id} ---")
        for item in top_trainings_scored: logger.info(f"  - {item['training'].training_id} ({item['training'].title}) | Score: {item['score']:.2f} | Sub-scores: {item['sub_scores']}")
            
        recommended_trainings = [{"training_id": t["training"].training_id} for t in top_trainings_scored]
        return {"predicted_type": "trainings_only", "trainings": recommended_trainings}

    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        trace_data = shared.get("trace_details", {})
        trace_data["training_ranking"] = self.ranked_trainings_for_tracing
        shared["trace_details"] = trace_data
        logger.info("Training-only recommendation stored in 'intermediate_recommendations'.")

# --- MAJOR REFACTOR: FindJobsAndTrainingsNode ---
class FindJobsAndTrainingsNode(Node):
    """
    Finds suitable jobs using the new Graduated Scoring architecture.
    """
    def prep(self, shared):
        profile = shared.get("persona_profile")
        jobs = shared.get("parsed_jobs")
        trainings = shared.get("parsed_trainings")
        if not all([profile, jobs, trainings]):
            raise ValueError("Persona profile, parsed jobs, or parsed trainings not found.")
        return {"profile": profile, "jobs": jobs, "trainings": trainings}

    def exec(self, prep_res: Dict) -> Dict[str, Any]:
        profile: PersonaProfile = prep_res["profile"]
        all_jobs: List[JobProfile] = prep_res["jobs"]
        all_trainings: List[TrainingProfile] = prep_res["trainings"]

        profile_dict = profile.model_dump()

        # Stage 1: Apply the forgiving safety net filter
        candidate_jobs = [
            job for job in all_jobs 
            if safety_net_filter(profile_dict, job.model_dump())
        ]
        logger.info(f"Found {len(candidate_jobs)} jobs after safety net filter.")

        if not candidate_jobs:
            logger.warning(f"No jobs passed the safety net for persona {profile.persona_id}. Returning empty.")
            return {"predicted_type": "jobs+trainings", "jobs": []}

        # Stage 2 & 3: Score all candidates and rank them
        scored_jobs = []
        for job in tqdm(candidate_jobs, desc=f"Scoring jobs for persona {profile.persona_id}", disable=len(candidate_jobs) < 10):
            job_dict = job.model_dump()
            composite_score, sub_scores = calculate_composite_score(profile_dict, job_dict)
            scored_jobs.append({"job": job, "score": composite_score, "sub_scores": sub_scores})

        sorted_jobs = sorted(scored_jobs, key=lambda x: x["score"], reverse=True)

        self.ranked_jobs_for_tracing = sorted_jobs
        # Stage 4: Select the Top 3 jobs
        top_jobs_scored = sorted_jobs[:3]
        
        logger.info(f"--- Top 3 Jobs for Persona {profile.persona_id} ---")
        for scored_job in top_jobs_scored:
            logger.info(
                f"  - Job: {scored_job['job'].job_id} ({scored_job['job'].title}) | "
                f"Composite Score: {scored_job['score']:.2f} | "
                f"Sub-scores: {scored_job['sub_scores']}"
            )

        # Stage 5: Find missing skills and trainings for ONLY the top jobs
        job_recommendations = []
        for scored_job in top_jobs_scored:
            job = scored_job["job"]
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
                            "trainings": matching_trainings[:3] # Limit to 3 trainings per skill
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
        trace_data = shared.get("trace_details", {})
        trace_data["job_ranking"] = self.ranked_jobs_for_tracing # Store the full ranked list
        shared["trace_details"] = trace_data
        logger.info("Jobs+trainings recommendation stored in 'intermediate_recommendations'.")
        
class FinalizeOutputNode(Node):
    # Unchanged
    def prep(self, shared):
        return {"persona_id": shared["persona_id"], "recs": shared["intermediate_recommendations"]}
    def exec(self, prep_res: Dict):
        return {"persona_id": prep_res["persona_id"], **prep_res["recs"]}
    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["final_recommendation"] = exec_res