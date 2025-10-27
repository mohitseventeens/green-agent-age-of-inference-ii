import logging
import json
from pathlib import Path  # <-- CORRECTED: Added the missing import
from pocketflow import Node
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional, Dict, Any
from tqdm import tqdm

from src.utils.data_retrieval import load_all_data
from src.utils.gdsc_utils import chat_with_persona
from src.utils.call_llm import call_llm

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
    """
    Parses raw job and training markdown files into structured Pydantic objects.
    Implements a file-based cache to avoid re-processing.
    """
    def _get_cache_path(self, name: str) -> Path:
        # Assumes the script runs from the project root.
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
        # Convert Pydantic models to dictionaries for JSON serialization
        dict_data = [item.model_dump() for item in data]
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, indent=2, ensure_ascii=False)

    def _parse_item(self, item: Dict[str, str], schema: Dict, item_id_key: str) -> Optional[Dict[str, Any]]:
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

    def exec(self, prep_res):
        parsed_jobs = self._load_from_cache("jobs", JobProfile)
        if not parsed_jobs:
            logger.info("Job cache not found. Parsing all jobs from markdown...")
            job_schema = JobProfile.model_json_schema()
            raw_jobs = self.shared.get("all_jobs", [])
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
            raw_trainings = self.shared.get("all_trainings", [])
            parsed_training_data = [
                self._parse_item(training, training_schema, "training_id") 
                for training in tqdm(raw_trainings, desc="Parsing Trainings")
            ]
            parsed_trainings = [TrainingProfile.model_validate(data) for data in parsed_training_data if data]
            self._save_to_cache("trainings", parsed_trainings)
            
        return {"parsed_jobs": parsed_jobs, "parsed_trainings": parsed_trainings}
        
    def post(self, shared, prep_res, exec_res):
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
        logger.info(f"Starting conversation with {persona_id}...")
        questions = [
            "Hello! To help you find the right green job opportunities, could you please tell me a bit about yourself? For example, your age and current city in Brazil.",
            "Great, thank you. What is your highest level of education, and what are some of your main skills or areas of experience?",
            "That's very helpful. Finally, what are your career goals? Are you actively looking for a job, interested in training, or just exploring options in the green economy?"
        ]
        conversation_id = None
        conversation_history = []
        for q in questions:
            logger.info(f"Asking: {q}")
            response_tuple = chat_with_persona(
                persona_id=persona_id, message=q, conversation_id=conversation_id
            )
            if response_tuple is None:
                raise RuntimeError(
                    "The chat_with_persona API call failed, likely due to expired AWS credentials. "
                    "Please refresh your temporary credentials and update your .env file or environment variables."
                )
            response, conversation_id = response_tuple
            logger.info(f"Response: {response}")
            conversation_history.append({"question": q, "answer": response})
        transcript = "\n".join([f"Q: {entry['question']}\nA: {entry['answer']}" for entry in conversation_history])
        schema = PersonaProfile.model_json_schema()
        extraction_prompt = f"""
        Analyze the conversation transcript and extract the user's profile into a valid JSON object that strictly follows this schema.
        JSON Schema:
        ---
        {json.dumps(schema, indent=2)}
        ---
        Conversation Transcript:
        ---
        {transcript}
        ---
        Respond ONLY with the JSON object. Do not include any other text or markdown formatting.
        """
        logger.info("Extracting profile from transcript using Pydantic schema...")
        profile_str = call_llm(prompt=extraction_prompt, use_cache=False)
        try:
            cleaned_str = profile_str.strip().replace("```json", "").replace("```", "")
            persona_profile = PersonaProfile.model_validate_json(cleaned_str)
        except ValidationError as e:
            logger.error(f"Pydantic validation failed for LLM output: {profile_str}")
            raise RuntimeError(f"Could not parse and validate persona profile from LLM. Validation errors: {e}")
        return {
            "persona_profile": persona_profile,
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
    """
    Formats the 'awareness' recommendation based on the decision action.
    """
    def prep(self, shared):
        decision = shared.get("decision_action")
        if not decision or "provide_awareness" not in decision:
            raise ValueError(f"Invalid decision action '{decision}' for ProvideAwarenessNode.")
        return decision

    def exec(self, decision: str) -> Dict[str, Any]:
        if decision == "provide_awareness_young":
            reason = "too_young"
            logger.info("Formatting awareness response for reason: too_young.")
        else: # Covers "provide_awareness_info"
            reason = "info"
            logger.info("Formatting awareness response for reason: info.")
            
        return {
            "predicted_type": "awareness",
            "predicted_items": reason
        }

    def post(self, shared, prep_res, exec_res: Dict[str, Any]):
        shared["intermediate_recommendations"] = exec_res
        logger.info(f"Awareness recommendation stored in 'intermediate_recommendations'.")