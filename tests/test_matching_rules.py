import pytest
from src.utils.matching_rules import (
    get_education_level,
    safety_net_filter,
    score_education_fit,
    score_experience_fit,
    score_location_preference,
    score_skills_match,
    calculate_composite_score
)

# --- Test Data Fixtures ---
@pytest.fixture
def sample_persona():
    return {
        "persona_id": "p1", "age": 25, "city": "São Paulo", "is_open_to_relocate": False,
        "education_level": "Graduação em produção com foco em equipamentos coletivos", # Level 5
        "experience_years": 3, "languages": ["Portuguese", "English"],
        "skills": ["Python", "Data Analysis", "Project Management"]
    }

@pytest.fixture
def sample_job():
    return {
        "job_id": "j1", "title": "Data Analyst", "city": "São Paulo", "is_remote": False,
        "education_level": "Graduação", # Level 5
        "experience_years": 2, "languages": ["Portuguese"],
        "required_skills": ["Python", "SQL", "Tableau"]
    }

# --- Tests for New Scoring Functions ---

def test_get_education_level():
    assert get_education_level("Ensino Médio") == 2
    assert get_education_level("Técnico em Eletrônica") == 3
    assert get_education_level("graduação (bachelor's degree)") == 5
    assert get_education_level("Pós-graduação") == 6
    assert get_education_level(None) is None
    assert get_education_level("Unknown Level") is None

def test_safety_net_filter(sample_persona, sample_job):
    assert safety_net_filter(sample_persona, sample_job) is True
    # Test language failure
    sample_job["languages"] = ["Spanish"]
    assert safety_net_filter(sample_persona, sample_job) is False
    # Test no language requirement
    sample_job["languages"] = []
    assert safety_net_filter(sample_persona, sample_job) is True

def test_score_education_fit():
    assert score_education_fit(5, 5) == 100  # Exact match
    assert score_education_fit(6, 5) == 100  # Overqualified
    assert score_education_fit(4, 5) == 70   # One level below
    assert score_education_fit(3, 5) == 40   # Two levels below
    assert score_education_fit(2, 5) == 10   # Big gap
    assert score_education_fit(5, None) == 80 # No job requirement
    assert score_education_fit(None, 5) == 40 # No persona education

def test_score_experience_fit():
    assert score_experience_fit(5, 3) == 100 # Overqualified
    assert score_experience_fit(2, 3) == 80  # 1 year less
    assert score_experience_fit(1, 3) == 50  # 2 years less
    assert score_experience_fit(0, 3) == 20  # 3 years less

def test_score_location_preference(sample_persona, sample_job):
    assert score_location_preference(sample_persona, sample_job) == 100 # Same city
    sample_job["is_remote"] = True
    assert score_location_preference(sample_persona, sample_job) == 100 # Remote
    sample_job["is_remote"] = False
    sample_job["city"] = "Recife"
    assert score_location_preference(sample_persona, sample_job) == 10  # Mismatch, not relocating
    sample_persona["is_open_to_relocate"] = True
    assert score_location_preference(sample_persona, sample_job) == 60 # Mismatch, but relocating

def test_score_skills_match():
    assert score_skills_match(["a", "b", "c"], ["a", "b", "d", "e"]) == 50 # 2 of 4 matched
    assert score_skills_match(["a", "b"], ["a", "b"]) == 100
    assert score_skills_match([], ["a", "b"]) == 0
    assert score_skills_match(["a", "b"], []) == 80 # No skills required

# --- Test for Composite Score ---

def test_calculate_composite_score(sample_persona, sample_job):
    score, sub_scores = calculate_composite_score(sample_persona, sample_job)
    
    # Persona: Edu 5, Exp 3, Skills ["Python", "Data Analysis", "Project Management"]
    # Job:     Edu 5, Exp 2, Skills ["Python", "SQL", "Tableau"]
    
    # Expected sub-scores:
    # Education: 100 (5 >= 5)
    # Experience: 100 (3 >= 2)
    # Location: 100 (São Paulo == São Paulo)
    # Skills: 33 (1 of 3 skills match: "Python")
    
    assert sub_scores['education'] == 100
    assert sub_scores['experience'] == 100
    assert sub_scores['location'] == 100
    assert sub_scores['skills'] == 33 # Rounded down from 33.33...
    
    # Expected weighted score:
    # (100 * 0.20) + (100 * 0.25) + (100 * 0.20) + (33 * 0.35)
    #   20         +    25        +    20        +   11.55 = 76.55
    expected_score = (100 * 0.20) + (100 * 0.25) + (100 * 0.20) + (33 * 0.35)
    
    assert score == round(expected_score, 2)
    print(f"\nCalculated composite score: {score}, Expected: {round(expected_score, 2)}")
    print(f"Sub-scores: {sub_scores}")