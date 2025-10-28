import logging
from typing import Dict, Any, List, Optional, Tuple
from src.utils.call_llm import call_llm # <-- ADD THIS IMPORT
import json # <-- ADD THIS IMPORT

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# # --- Education Levels Hierarchy (Unchanged) ---
# EDUCATION_LEVELS = {
#     "Ensino Fundamental": 1, "Ensino Médio": 2, "Técnico": 3, "Tecnólogo": 4,
#     "Graduação": 5, "Pós-graduação": 6, "Mestrado": 7, "Doutorado": 8,
#     "Bacharelado": 5, "Licenciatura": 5, "Especialização": 6, "MBA": 7,
#     "ensino fundamental": 1, "ensino medio": 2, "técnico": 3, "tecnólogo": 4,
#     "graduação": 5, "bacharelado": 5, "pos-graduacao": 6, "mestrado": 7,
# }

# def get_education_level(level_str: Optional[str]) -> Optional[int]:
#     if not level_str: return None
#     level_str_lower = level_str.lower()
#     if 'doutorado' in level_str_lower: return 8
#     if 'mestrado' in level_str_lower or 'mba' in level_str_lower: return 7
#     if 'pós-graduação' in level_str_lower or 'pos-graduacao' in level_str_lower or 'especialização' in level_str_lower: return 6
#     if 'graduação' in level_str_lower or 'graduacao' in level_str_lower or 'bacharelado' in level_str_lower or 'superior' in level_str_lower: return 5
#     if 'tecnólogo' in level_str_lower or 'tecnologo' in level_str_lower: return 4
#     if 'técnico' in level_str_lower or 'tecnico' in level_str_lower: return 3
#     if 'médio' in level_str_lower or 'medio' in level_str_lower: return 2
#     if 'fundamental' in level_str_lower: return 1
#     return None

# # --- Job Scoring Functions (Unchanged) ---
# def safety_net_filter(persona: Dict[str, Any], job: Dict[str, Any]) -> bool:
#     persona_langs = set(lang.lower() for lang in persona.get("languages", ["portuguese"]))
#     job_langs_req = set(lang.lower() for lang in job.get("languages", []))
#     if job_langs_req and not persona_langs.intersection(job_langs_req):
#         return False
#     return True

# def score_education_fit(persona_level: Optional[int], job_level: Optional[int]) -> int:
#     if job_level is None: return 80
#     if persona_level is None: return 40
#     diff = persona_level - job_level
#     if diff >= 0: return 100
#     if diff == -1: return 70
#     if diff == -2: return 40
#     return 10

# def score_experience_fit(persona_years: int, job_years: int) -> int:
#     diff = persona_years - job_years
#     if diff >= 0: return 100
#     if diff >= -1: return 80
#     if diff >= -2: return 50
#     return 20

# def score_location_preference(persona: Dict[str, Any], job: Dict[str, Any]) -> int:
#     if job.get("is_remote"): return 100
#     if persona.get("city") == job.get("city"): return 100
#     if persona.get("is_open_to_relocate"): return 60
#     return 10

# def score_skills_match(persona_skills: List[str], job_skills: List[str]) -> int:
#     if not job_skills: return 80
#     persona_set = set(s.lower().strip() for s in persona_skills)
#     job_set = set(s.lower().strip() for s in job_skills)
#     intersection = persona_set.intersection(job_set)
#     return int((len(intersection) / len(job_set)) * 100) if job_set else 0

# def calculate_composite_score(persona: Dict[str, Any], job: Dict[str, Any]) -> Tuple[float, Dict[str, int]]:
#     persona_edu_level = get_education_level(persona.get("education_level"))
#     job_edu_level = get_education_level(job.get("education_level"))
#     sub_scores = {
#         'education': score_education_fit(persona_edu_level, job_edu_level),
#         'experience': score_experience_fit(persona.get("experience_years", 0), job.get("experience_years", 0)),
#         'location': score_location_preference(persona, job),
#         'skills': score_skills_match(persona.get("skills", []), job.get("required_skills", []))
#     }
#     weights = {'education': 0.20, 'experience': 0.25, 'location': 0.20, 'skills': 0.35}
#     composite = sum(sub_scores[dim] * weights[dim] for dim in sub_scores)
#     return round(composite, 2), sub_scores

# def get_required_trainings(persona: Dict[str, Any], job: Dict[str, Any]) -> List[str]:
#     persona_skills = set(skill.lower() for skill in persona.get("skills", []))
#     job_skills_req = set(skill.lower() for skill in job.get("required_skills", []))
#     return list(job_skills_req - persona_skills)


# # --- NEW: Training Scoring Functions ---

# def score_training_prerequisite_fit(persona_level: Optional[int], training_level: Optional[int]) -> int:
#     """
#     Scores how well a persona's education level matches a training's prerequisite.
#     It strongly favors trainings at the persona's level, the next level up, or with no prerequisite.
#     """
#     if training_level is None or training_level == 0:
#         return 100  # Open to all, perfect fit.
#     if persona_level is None:
#         return 30 # Persona has no formal education, less ideal for specific prerequisites.
        
#     diff = training_level - persona_level
#     if diff == 0: return 100 # Prerequisite is at the user's current level.
#     if diff == 1: return 100 # Prerequisite is the next logical step up.
#     if diff > 1: return 20   # Prerequisite is too advanced.
#     if diff < 0: return 60   # Persona is overqualified, but that's okay.
#     return 50 # Default case

# def score_training_goal_alignment(persona_goals: str, training_title: str, training_skills: List[str]) -> int:
#     """Uses a cheap LLM call to get a semantic score for goal alignment."""
#     prompt = f'On a scale of 0-100, how well does this training align with the persona goal? Goal: "{persona_goals}". Training: "{training_title}" (offers skills: {training_skills}). Respond ONLY with JSON: {{"score": N}}'
#     try:
#         response_str = call_llm(prompt, model="mistral-small-latest", use_cache=True)
#         return int(json.loads(response_str.strip().replace("```json", "").replace("```", "")).get("score", 0))
#     except (json.JSONDecodeError, ValueError, Exception) as e:
#         logger.warning(f"Could not parse goal alignment score for training '{training_title}': {e}")
#         return 0

# def calculate_training_composite_score(persona: Dict[str, Any], training: Dict[str, Any]) -> Tuple[float, Dict[str, int]]:
#     """Calculates a weighted composite score for a training."""
#     persona_edu_level = get_education_level(persona.get("education_level"))
#     training_req_level = get_education_level(training.get("required_level"))
    
#     sub_scores = {
#         'prerequisite': score_training_prerequisite_fit(persona_edu_level, training_req_level),
#         'goal_alignment': score_training_goal_alignment(persona.get("goals", ""), training.get("title", ""), training.get("offered_skills", []))
#     }
    
#     weights = {
#         'prerequisite': 0.40,
#         'goal_alignment': 0.60, # Goal alignment is more important
#     }
    
#     composite = sum(sub_scores[dim] * weights[dim] for dim in sub_scores)
#     return round(composite, 2), sub_scores


EDUCATION_LEVELS = {
    "Ensino Fundamental": 1, "Ensino Médio": 2, "Técnico": 3, "Tecnólogo": 4,
    "Graduação": 5, "Pós-graduação": 6, "Mestrado": 7, "Doutorado": 8,
    "Bacharelado": 5, "Licenciatura": 5, "Especialização": 6, "MBA": 7,
    "ensino fundamental": 1, "ensino medio": 2, "técnico": 3, "tecnólogo": 4,
    "graduação": 5, "bacharelado": 5, "pos-graduacao": 6, "mestrado": 7,
}

def get_education_level(level_str: Optional[str]) -> Optional[int]:
    if not level_str: return None
    # ... (function is unchanged)
    level_str_lower = level_str.lower()
    if 'doutorado' in level_str_lower: return 8
    if 'mestrado' in level_str_lower or 'mba' in level_str_lower: return 7
    if 'pós-graduação' in level_str_lower or 'pos-graduacao' in level_str_lower or 'especialização' in level_str_lower: return 6
    if 'graduação' in level_str_lower or 'graduacao' in level_str_lower or 'bacharelado' in level_str_lower or 'superior' in level_str_lower: return 5
    if 'tecnólogo' in level_str_lower or 'tecnologo' in level_str_lower: return 4
    if 'técnico' in level_str_lower or 'tecnico' in level_str_lower: return 3
    if 'médio' in level_str_lower or 'medio' in level_str_lower: return 2
    if 'fundamental' in level_str_lower: return 1
    return None

# --- Job Scoring Functions ---
def safety_net_filter(persona: Dict[str, Any], job: Dict[str, Any]) -> bool:
    # ... (function is unchanged)
    persona_langs = set(lang.lower() for lang in persona.get("languages", ["portuguese"]))
    job_langs_req = set(lang.lower() for lang in job.get("languages", []))
    if job_langs_req and not persona_langs.intersection(job_langs_req):
        return False
    return True

# --- NEW: LLM-based Goal Scorer ---
def score_goal_alignment(persona_goals: str, job_title: str, job_skills: List[str]) -> int:
    """
    Uses a powerful LLM to get a semantic score for goal alignment.
    This is the most important (and expensive) part of the scoring.
    """
    prompt = f"""
    On a scale of 0 to 100, how well does this job align with the persona's stated career goal?
    - A score of 90-100 means a perfect or near-perfect match in the desired industry and role.
    - A score of 60-89 means a reasonable match in a related industry or a slightly different role.
    - A score below 60 means it is not a relevant match.

    Persona's Goal: "{persona_goals}"
    Job Title: "{job_title}"
    Job's Required Skills: {job_skills}

    Respond ONLY with a valid JSON object like {{"score": N}}.
    """
    try:
        # Use a powerful model for this nuanced task. Caching is critical.
        response_str = call_llm(prompt, model="mistral-large-latest", use_cache=True)
        return int(json.loads(response_str.strip().replace("```json", "").replace("```", "")).get("score", 0))
    except (json.JSONDecodeError, ValueError, Exception) as e:
        logger.warning(f"Could not parse GOAL ALIGNMENT score for job '{job_title}': {e}")
        return 0

# (score_education_fit, score_experience_fit, score_location_preference, score_skills_match are unchanged)
def score_education_fit(persona_level: Optional[int], job_level: Optional[int]) -> int: #...
    if job_level is None: return 80
    if persona_level is None: return 40
    diff = persona_level - job_level
    if diff >= 0: return 100
    if diff == -1: return 70
    if diff == -2: return 40
    return 10
def score_experience_fit(persona_years: int, job_years: int) -> int: #...
    diff = persona_years - job_years
    if diff >= 0: return 100
    if diff >= -1: return 80
    if diff >= -2: return 50
    return 20
def score_location_preference(persona: Dict[str, Any], job: Dict[str, Any]) -> int: #...
    if job.get("is_remote"): return 100
    if persona.get("city") == job.get("city"): return 100
    if persona.get("is_open_to_relocate"): return 60
    return 10
def score_skills_match(persona_skills: List[str], job_skills: List[str]) -> int: #...
    if not job_skills: return 80
    persona_set = set(s.lower().strip() for s in persona_skills)
    job_set = set(s.lower().strip() for s in job_skills)
    intersection = persona_set.intersection(job_set)
    return int((len(intersection) / len(job_set)) * 100) if job_set else 0

# --- MODIFIED: calculate_composite_score ---
def calculate_composite_score(persona: Dict[str, Any], job: Dict[str, Any]) -> Tuple[float, Dict[str, int]]:
    """
    Calculates a weighted composite score, now including Goal Alignment.
    """
    persona_edu_level = get_education_level(persona.get("education_level"))
    job_edu_level = get_education_level(job.get("education_level"))
    
    sub_scores = {
        'goals': score_goal_alignment(persona.get("goals", ""), job.get("title", ""), job.get("required_skills", [])),
        'skills': score_skills_match(persona.get("skills", []), job.get("required_skills", [])),
        'experience': score_experience_fit(persona.get("experience_years", 0), job.get("experience_years", 0)),
        'education': score_education_fit(persona_edu_level, job_edu_level),
        'location': score_location_preference(persona, job)
    }
    
    # Re-tuned weights to heavily prioritize goal alignment
    weights = {
        'goals': 0.50,      # <-- MOST IMPORTANT FACTOR
        'skills': 0.20,     # Still important
        'experience': 0.15,
        'education': 0.10,
        'location': 0.05,   # Least important, as many jobs are remote
    }
    
    composite = sum(sub_scores[dim] * weights[dim] for dim in sub_scores)
    return round(composite, 2), sub_scores

# (get_required_trainings and training scoring functions are unchanged)
def get_required_trainings(persona, job): #...
    persona_skills = set(skill.lower() for skill in persona.get("skills", []))
    job_skills_req = set(skill.lower() for skill in job.get("required_skills", []))
    return list(job_skills_req - persona_skills)
def score_training_prerequisite_fit(persona_level, training_level): #...
    if training_level is None or training_level == 0: return 100
    if persona_level is None: return 30
    diff = training_level - persona_level
    if diff == 0: return 100
    if diff == 1: return 100
    if diff > 1: return 20
    if diff < 0: return 60
    return 50
def score_training_goal_alignment(persona_goals, training_title, training_skills): #...
    prompt = f'On a scale of 0-100, how well does this training align with the persona goal? Goal: "{persona_goals}". Training: "{training_title}" (offers skills: {training_skills}). Respond ONLY with JSON: {{"score": N}}'
    try:
        response_str = call_llm(prompt, model="mistral-small-latest", use_cache=True)
        return int(json.loads(response_str.strip().replace("```json", "").replace("```", "")).get("score", 0))
    except Exception: return 0
def calculate_training_composite_score(persona, training): #...
    persona_edu_level = get_education_level(persona.get("education_level"))
    training_req_level = get_education_level(training.get("required_level"))
    sub_scores = {'prerequisite': score_training_prerequisite_fit(persona_edu_level, training_req_level), 'goal_alignment': score_training_goal_alignment(persona.get("goals", ""), training.get("title", ""), training.get("offered_skills", []))}
    weights = {'prerequisite': 0.40, 'goal_alignment': 0.60}
    composite = sum(sub_scores[dim] * weights[dim] for dim in sub_scores)
    return round(composite, 2), sub_scores

def keyword_relevance_filter(persona: Dict[str, Any], training: Dict[str, Any], threshold: float = 0.1) -> bool:
    """
    Fast, non-LLM keyword-based filter to check for coarse relevance.
    Returns True if the training seems somewhat relevant to the persona's goals/skills.
    """
    persona_text = " ".join([
        persona.get("goals", ""),
        " ".join(persona.get("skills", []))
    ]).lower()
    
    training_text = " ".join([
        training.get("title", ""),
        " ".join(training.get("offered_skills", []))
    ]).lower()

    # Simple word tokenization
    persona_words = set(persona_text.split())
    training_words = set(training_text.split())

    # Remove common stopwords to improve signal
    stopwords = {'de', 'da', 'do', 'em', 'para', 'com', 'e', 'o', 'a', 'que', 'um', 'uma',
                 'the', 'and', 'or', 'in', 'to', 'for', 'of', 'is', 'with'}
    persona_words -= stopwords
    training_words -= stopwords
    
    # Handle cases with no keywords
    if not persona_words or not training_words:
        return True # Be lenient if we have no text to compare

    overlap = len(persona_words.intersection(training_words))
    # We check for any overlap as a simple starting point.
    # A more advanced version could use a ratio.
    return overlap > 0