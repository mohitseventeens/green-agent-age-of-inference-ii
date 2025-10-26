import logging
from typing import Dict, Any, List

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- Brazilian Education Levels Hierarchy ---
# A higher number indicates a higher level of education.
EDUCATION_LEVELS = {
    "Ensino Fundamental": 1,
    "Ensino Médio": 2,
    "Técnico": 3,
    "Tecnólogo": 4,
    "Graduação": 5,
    "Bacharelado": 5, # Equivalent to Graduação
    "Licenciatura": 5, # Equivalent to Graduação
    "Pós-graduação": 6,
    "Especialização": 6, # Equivalent to Pós-graduação
    "Mestrado": 7,
    "MBA": 7, # Often considered equivalent to Mestrado in a business context
    "Doutorado": 8,
    # Add common variations to handle messy data
    "ensino fundamental": 1,
    "ensino medio": 2,
    "tecnico": 3,
    "tecnologo": 4,
    "graduacao": 5,
    "bacharelado": 5,
    "licenciatura": 5,
    "pos-graduacao": 6,
    "especializacao": 6,
    "mestrado": 7,
    "mba": 7,
    "doutorado": 8,
}

def apply_hard_filters(persona: Dict[str, Any], job: Dict[str, Any]) -> bool:
    """
    Applies strict matching rules to determine if a job is a fit for a persona.

    Args:
        persona: A dictionary representing the persona's profile.
        job: A dictionary representing the job's requirements.

    Returns:
        True if the job passes all hard filters, False otherwise.
    """
    # 1. Location Filter
    is_job_remote = job.get("is_remote", False)
    persona_open_to_relocate = persona.get("is_open_to_relocate", False)
    if not is_job_remote and not persona_open_to_relocate:
        if persona.get("city") != job.get("city"):
            logger.debug(f"Filter FAIL (Location): Job city {job.get('city')} != Persona city {persona.get('city')}")
            return False

    # 2. Education Filter
    persona_edu_level = EDUCATION_LEVELS.get(persona.get("education_level", "").strip(), 0)
    job_edu_req = EDUCATION_LEVELS.get(job.get("education_level", "").strip(), 0)
    if persona_edu_level < job_edu_req:
        logger.debug(f"Filter FAIL (Education): Persona level {persona_edu_level} < Job level {job_edu_req}")
        return False
        
    # 3. Experience Filter
    persona_exp = persona.get("experience_years", 0)
    job_exp_req = job.get("experience_years", 0)
    if persona_exp < job_exp_req:
        logger.debug(f"Filter FAIL (Experience): Persona years {persona_exp} < Job years {job_exp_req}")
        return False

    # 4. Language Filter (simplified: checks for at least one common language)
    persona_langs = set(lang.lower() for lang in persona.get("languages", []))
    job_langs_req = set(lang.lower() for lang in job.get("languages", []))
    if job_langs_req and not persona_langs.intersection(job_langs_req):
        logger.debug(f"Filter FAIL (Language): No common language between {persona_langs} and {job_langs_req}")
        return False

    # If all checks pass
    logger.debug("Filter PASS: All hard filters met.")
    return True

def get_required_trainings(persona: Dict[str, Any], job: Dict[str, Any]) -> List[str]:
    """
    Identifies trainings needed for a persona to meet job skill requirements.
    
    NOTE: This is a simplified initial implementation. It only identifies missing
    skills and does not yet handle the sequential level progression.

    Args:
        persona: A dictionary representing the persona's profile.
        job: A dictionary representing the job's requirements.

    Returns:
        A list of skill names for which training is required.
    """
    persona_skills = set(skill.lower() for skill in persona.get("skills", []))
    job_skills_req = set(skill.lower() for skill in job.get("required_skills", []))
    
    missing_skills = list(job_skills_req - persona_skills)
    logger.debug(f"Identified missing skills: {missing_skills}")
    return missing_skills
