import pytest
from src.utils.matching_rules import apply_hard_filters, get_required_trainings

# --- Test Data Fixtures ---
@pytest.fixture
def sample_persona():
    """A sample persona profile for testing."""
    return {
        "city": "São Paulo",
        "education_level": "Graduação",
        "experience_years": 3,
        "languages": ["Portuguese", "English"],
        "is_open_to_relocate": False,
        "skills": ["Python", "Data Analysis"]
    }

@pytest.fixture
def sample_job():
    """A perfectly matching job for the sample persona."""
    return {
        "city": "São Paulo",
        "is_remote": False,
        "education_level": "Graduação",
        "experience_years": 2,
        "languages": ["Portuguese"],
        "required_skills": ["Python", "SQL"]
    }

# --- Tests for apply_hard_filters ---

def test_filters_pass_on_perfect_match(sample_persona, sample_job):
    assert apply_hard_filters(sample_persona, sample_job) == True

def test_filter_fails_on_location(sample_persona, sample_job):
    sample_job["city"] = "Recife"
    assert apply_hard_filters(sample_persona, sample_job) == False

def test_filter_passes_on_location_if_remote(sample_persona, sample_job):
    sample_job["city"] = "Recife"
    sample_job["is_remote"] = True
    assert apply_hard_filters(sample_persona, sample_job) == True

def test_filter_passes_on_location_if_relocate(sample_persona, sample_job):
    sample_persona["is_open_to_relocate"] = True
    sample_job["city"] = "Recife"
    assert apply_hard_filters(sample_persona, sample_job) == True

def test_filter_fails_on_education(sample_persona, sample_job):
    sample_job["education_level"] = "Mestrado"
    assert apply_hard_filters(sample_persona, sample_job) == False

def test_filter_passes_on_lower_education_req(sample_persona, sample_job):
    sample_job["education_level"] = "Técnico"
    assert apply_hard_filters(sample_persona, sample_job) == True

def test_filter_fails_on_experience(sample_persona, sample_job):
    sample_job["experience_years"] = 5
    assert apply_hard_filters(sample_persona, sample_job) == False
    
def test_filter_fails_on_language(sample_persona, sample_job):
    sample_job["languages"] = ["Spanish"]
    assert apply_hard_filters(sample_persona, sample_job) == False

def test_filter_passes_on_language_intersection(sample_persona, sample_job):
    sample_job["languages"] = ["English", "Spanish"]
    assert apply_hard_filters(sample_persona, sample_job) == True

# --- Tests for get_required_trainings ---

def test_trainings_identifies_missing_skill(sample_persona, sample_job):
    missing = get_required_trainings(sample_persona, sample_job)
    assert isinstance(missing, list)
    assert len(missing) == 1
    assert "sql" in missing

def test_trainings_returns_empty_when_no_skills_missing(sample_persona, sample_job):
    sample_persona["skills"].append("SQL")
    missing = get_required_trainings(sample_persona, sample_job)
    assert len(missing) == 0

def test_trainings_returns_empty_when_job_has_no_reqs(sample_persona, sample_job):
    sample_job["required_skills"] = []
    missing = get_required_trainings(sample_persona, sample_job)
    assert len(missing) == 0
