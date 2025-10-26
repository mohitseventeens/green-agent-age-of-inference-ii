import logging
import json
from pocketflow import Node
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

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

# --- Pydantic Data Model for Persona Profile ---
class PersonaProfile(BaseModel):
    """Defines the structured data for a user's profile."""
    age: int = Field(..., description="The persona's age in years.")
    city: str = Field(..., description="The primary city where the persona lives.")
    education_level: str = Field(..., description="The highest level of education achieved, e.g., 'Ensino Fundamental'.")
    experience_years: int = Field(..., description="Estimated years of professional experience.")
    skills: List[str] = Field(..., description="A list of key skills the persona mentioned.")
    goals: str = Field(..., description="A summary of the persona's career goals or immediate intentions.")
    is_open_to_relocate: bool = Field(..., description="Whether the persona is willing to relocate for a job.")
    languages: List[str] = Field(default=["Portuguese"], description="List of languages the persona speaks.")


class LoadStaticDataNode(Node):
    """
    A node that loads all job and training data from local markdown files
    into the shared store at the beginning of a flow.
    """
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

class ExtractProfileNode(Node):
    """
    Conducts a conversation with a persona to extract a Pydantic-validated profile.
    """
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
    """
    Analyzes the persona's profile and determines the next step in the flow.
    Returns an action string for conditional routing.
    """
    def prep(self, shared):
        profile = shared.get("persona_profile")
        if not profile or not isinstance(profile, PersonaProfile):
            raise ValueError("A valid PersonaProfile object was not found in the shared store.")
        return profile

    def exec(self, profile: PersonaProfile) -> str:
        logger.info(f"Making decision for persona with age {profile.age} and goals: '{profile.goals}'")
        
        # Rule 1: Age-based awareness
        if profile.age < 16:
            logger.info("Decision: provide_awareness_young (age < 16)")
            return "provide_awareness_young"
        
        # Rule 2: Goal-based awareness (informational)
        informational_keywords = ["exploring", "explorar", "curious", "curioso", "just looking", "só olhando", "not sure", "não sei"]
        if any(keyword in profile.goals.lower() for keyword in informational_keywords):
            logger.info("Decision: provide_awareness_info (informational goals)")
            return "provide_awareness_info"
            
        # Rule 3: Trainings only
        training_keywords = ["training", "treinamento", "courses", "cursos", "learn", "aprender", "study", "estudar", "upskill"]
        job_keywords = ["job", "emprego", "work", "trabalhar", "career", "carreira"]
        
        has_training_goal = any(keyword in profile.goals.lower() for keyword in training_keywords)
        has_job_goal = any(keyword in profile.goals.lower() for keyword in job_keywords)

        if has_training_goal and not has_job_goal:
            logger.info("Decision: recommend_trainings (training-focused goals)")
            return "recommend_trainings"

        # Rule 4: Default to jobs + trainings
        logger.info("Decision: recommend_jobs (default path)")
        return "recommend_jobs"

    def post(self, shared, prep_res, exec_res: str) -> Optional[str]:
        shared["decision_action"] = exec_res
        logger.info(f"Decision action '{exec_res}' stored in shared store.")
        # This return value is used by the Flow to determine the next node
        return exec_res