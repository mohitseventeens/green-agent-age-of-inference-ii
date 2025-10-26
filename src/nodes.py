import logging
import json
from pocketflow import Node
from pydantic import BaseModel, Field, ValidationError
from typing import List

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
            
            # Call the utility function
            response_tuple = chat_with_persona(
                persona_id=persona_id, message=q, conversation_id=conversation_id
            )
            
            # --- ROBUSTNESS CHECK ---
            # Check if the API call failed (the utility returns None on failure)
            if response_tuple is None:
                raise RuntimeError(
                    "The chat_with_persona API call failed, likely due to expired AWS credentials. "
                    "Please refresh your temporary credentials and update your .env file or environment variables."
                )
            
            # If the check passes, unpack the tuple
            response, conversation_id = response_tuple
            # --- END OF CHECK ---

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