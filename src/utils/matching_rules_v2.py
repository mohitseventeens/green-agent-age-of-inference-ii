import logging
from typing import Dict, Any, List, Optional, Tuple

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- NEW: Expanded and Normalized Education Levels Hierarchy ---
# This is now more robust to handle the variations seen in the data analysis.
# A higher number indicates a higher level of education.
EDUCATION_LEVELS = {
    # Formal Levels (Canonical)
    "Ensino Fundamental": 1,
    "Ensino Médio": 2,
    "Técnico": 3,
    "Tecnólogo": 4,
    "Graduação": 5,
    "Pós-graduação": 6,
    "Mestrado": 7,
    "Doutorado": 8,

    # Common Aliases and Equivalents
    "Bacharelado": 5,
    "Licenciatura": 5,
    "Especialização": 6,
    "MBA": 7,

    # Lowercase and common variations from parsed data
    "ensino fundamental": 1,
    "ensino medio": 2,
    "técnico": 3,
    "tecnólogo": 4,
    "graduação": 5,
    "bacharelado": 5,
    "pos-graduacao": 6,
    "mestrado": 7,
}

def get_education_level(level_str: Optional[str]) -> Optional[int]:
    """
    Safely gets the numeric education level for a given string,
    handling variations and returning None if not found.
    """
    if not level_str:
        return None
    # Simple brute-force check for keywords in the messy strings
    # This is a pragmatic way to handle the observed data variations.
    level_str_lower = level_str.lower()
    if 'doutorado' in level_str_lower: return 8
    if 'mestrado' in level_str_lower or 'mba' in level_str_lower: return 7
    if 'pós-graduação' in level_str_lower or 'pos-graduacao' in level_str_lower or 'especialização' in level_str_lower: return 6
    if 'graduação' in level_str_lower or 'graduacao' in level_str_lower or 'bacharelado' in level_str_lower or 'superior' in level_str_lower: return 5
    if 'tecnólogo' in level_str_lower or 'tecnologo' in level_str_lower: return 4
    if 'técnico' in level_str_lower or 'tecnico' in level_str_lower: return 3
    if 'médio' in level_str_lower or 'medio' in level_str_lower: return 2
    if 'fundamental' in level_str_lower: return 1
    return None # Return None if no keywords match

# --- 1. Safety Net Filter (Replaces apply_hard_filters) ---
def safety_net_filter(persona: Dict[str, Any], job: Dict[str, Any]) -> bool:
    """
    Applies minimal "safety net" filters to eliminate only truly impossible matches.
    Education and Experience are NOT checked here; they are handled by scoring.
    """
    # Language Filter: Eliminates only if there's a requirement and no overlap.
    persona_langs = set(lang.lower() for lang in persona.get("languages", ["portuguese"]))
    job_langs_req = set(lang.lower() for lang in job.get("languages", []))
    
    if job_langs_req and not persona_langs.intersection(job_langs_req):
        logger.debug(f"Safety Net FAIL (Language): Job {job.get('job_id')} requires {job_langs_req}, persona has {persona_langs}")
        return False
        
    logger.debug(f"Safety Net PASS: Job {job.get('job_id')} passed language filter.")
    return True

# --- 2. Multi-Dimensional Scoring Functions ---
def score_education_fit(persona_level: Optional[int], job_level: Optional[int]) -> int:
    """
    Tolerant scoring that rewards overqualification and penalizes
    underqualification gradually. Returns a score from 0 to 100.
    """
    if job_level is None:
        return 80  # Job has no requirement, so it's a good fit.
    if persona_level is None:
        return 40 # Persona has no formal education, a neutral-low score.

    diff = persona_level - job_level
    if diff >= 0: return 100 # Meets or exceeds requirement
    if diff == -1: return 70  # One level below: still quite good (trainable)
    if diff == -2: return 40  # Two levels below: possible but needs training
    return 10                # Big gap: unlikely fit

def score_experience_fit(persona_years: int, job_years: int) -> int:
    """Graduated scoring for experience. Returns a score from 0 to 100."""
    diff = persona_years - job_years
    if diff >= 0: return 100   # Meets or exceeds
    if diff >= -1: return 80   # Up to 1 year less: very viable
    if diff >= -2: return 50   # Up to 2 years less: possible
    return 20                  # Big gap: unlikely

def score_location_preference(persona: Dict[str, Any], job: Dict[str, Any]) -> int:
    """Scores location fit based on remote, city match, and relocation preference."""
    if job.get("is_remote"):
        return 100
    if persona.get("city") == job.get("city"):
        return 100
    # A forgiving check for state could be added here if we had state data.
    if persona.get("is_open_to_relocate"):
        return 60 # Good, but not as good as being local already.
    return 10 # Mismatch and not willing to relocate.

def score_skills_match(persona_skills: List[str], job_skills: List[str]) -> int:
    """Calculates a skill match score based on overlap."""
    if not job_skills:
        return 80 # No specific skills required, good fit.
    
    persona_set = set(s.lower().strip() for s in persona_skills)
    job_set = set(s.lower().strip() for s in job_skills)
    
    intersection = persona_set.intersection(job_set)
    
    # Jaccard Index: (size of intersection) / (size of union)
    # This rewards overlap while penalizing for many uncovered requirements.
    # union = persona_set.union(job_set)
    # score = int((len(intersection) / len(union)) * 100) if union else 0

    # Simpler overlap percentage: (skills you have) / (skills they want)
    score = int((len(intersection) / len(job_set)) * 100) if job_set else 0
    return score

# --- 3. Weighted Composite Score ---
def calculate_composite_score(persona: Dict[str, Any], job: Dict[str, Any]) -> Tuple[float, Dict[str, int]]:
    """
    Calculates a weighted composite score based on multiple dimensions of fit.
    """
    persona_edu_level = get_education_level(persona.get("education_level"))
    job_edu_level = get_education_level(job.get("education_level"))
    
    sub_scores = {
        'education': score_education_fit(persona_edu_level, job_edu_level),
        'experience': score_experience_fit(persona.get("experience_years", 0), job.get("experience_years", 0)),
        'location': score_location_preference(persona, job),
        'skills': score_skills_match(persona.get("skills", []), job.get("required_skills", []))
    }
    
    # These weights can be tuned based on priorities.
    weights = {
        'education': 0.20,
        'experience': 0.25,
        'location': 0.20,
        'skills': 0.35, # Skills are the most important factor
    }
    
    composite = sum(sub_scores[dim] * weights[dim] for dim in sub_scores)
    return round(composite, 2), sub_scores


# --- Legacy function, kept for reference/potential reuse in a different context ---
def get_required_trainings(persona: Dict[str, Any], job: Dict[str, Any]) -> List[str]:
    """
    Identifies trainings needed for a persona to meet job skill requirements.
    """
    persona_skills = set(skill.lower() for skill in persona.get("skills", []))
    job_skills_req = set(skill.lower() for skill in job.get("required_skills", []))
    
    missing_skills = list(job_skills_req - persona_skills)
    logger.debug(f"Identified missing skills: {missing_skills}")
    return missing_skills