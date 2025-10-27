import pytest
import os
import json
import getpass
from pathlib import Path
from src.nodes import LoadStaticDataNode, ExtractProfileNode, DecisionNode, ParseStaticDataNode, PersonaProfile, JobProfile, TrainingProfile
from src.utils.matching_rules import EDUCATION_LEVELS
from dotenv import load_dotenv

# --- Load .env file for MISTRAL_API_KEY ---
load_dotenv()

# --- REFACTORED: Credential Loading as a Fixture ---
@pytest.fixture(scope="session", autouse=True)
def manage_credentials(request):
    """
    A session-wide fixture to manage credentials. It only prompts for AWS
    credentials if a test marked with 'requires_aws_creds' is selected to run.
    """
    if request.node.get_closest_marker("requires_aws_creds"):
        print("\n(An AWS-dependent test is running, checking credentials...)")
        creds_to_check = {
            "AWS_ACCESS_KEY_ID": "Enter your AWS Access Key ID: ",
            "AWS_SECRET_ACCESS_KEY": "Enter your AWS Secret Access Key: ",
            "AWS_SESSION_TOKEN": "Enter your AWS Session Token: "
        }
        for key, prompt_text in creds_to_check.items():
            if not os.getenv(key):
                print(f"Environment variable '{key}' not found.")
                value = getpass.getpass(prompt_text)
                os.environ[key] = value
                print(f"✅ '{key}' set for this session.")

# This marker will now trigger the fixture above.
requires_aws_creds = pytest.mark.skipif(
    not os.getenv("AWS_ACCESS_KEY_ID") or not os.getenv("AWS_SECRET_ACCESS_KEY"),
    reason="This test makes a live API call and requires AWS credentials."
)
# Ensure Mistral key is present for tests that need it.
requires_mistral_key = pytest.mark.skipif(
    not os.getenv("MISTRAL_API_KEY"),
    reason="This test requires the MISTRAL_API_KEY."
)

# --- Fixture to clean up cache files ---
@pytest.fixture
def cleanup_cache_files():
    yield
    print("\nCleaning up cache files...")
    job_cache = Path("data/parsed_jobs.json")
    training_cache = Path("data/parsed_trainings.json")
    if job_cache.exists():
        job_cache.unlink()
        print("Removed job cache.")
    if training_cache.exists():
        training_cache.unlink()
        print("Removed training cache.")

# --- OPTIMIZED: Test for ParseStaticDataNode ---
@requires_mistral_key
def test_parse_static_data_node(cleanup_cache_files):
    """
    Tests the ParseStaticDataNode on a small subset of data.
    It verifies both parsing from markdown and reading from the created cache.
    """
    # Arrange: Create a small subset of the real data for testing
    load_node = LoadStaticDataNode()
    shared_full = {}
    load_node.run(shared_full)
    
    # OPTIMIZATION: Use only a small slice of the data
    test_jobs_raw = shared_full["all_jobs"][:5]
    test_trainings_raw = shared_full["all_trainings"][:5]
    
    # --- 1. First Run: Parsing the subset ---
    print("\n--- Running ParseStaticDataNode (First Run): Parsing 5 jobs & 5 trainings ---")
    shared = {"all_jobs": test_jobs_raw, "all_trainings": test_trainings_raw}
    parse_node = ParseStaticDataNode()
    parse_node.shared = shared
    parse_node.run(shared)

    # Assert parsing worked and cache files were created
    assert "parsed_jobs" in shared
    assert "parsed_trainings" in shared
    assert len(shared["parsed_jobs"]) == 5
    assert len(shared["parsed_trainings"]) == 5
    assert isinstance(shared["parsed_jobs"][0], JobProfile)
    assert isinstance(shared["parsed_trainings"][0], TrainingProfile)
    assert Path("data/parsed_jobs.json").exists()
    assert Path("data/parsed_trainings.json").exists()

    # --- 2. Second Run: Reading from cache ---
    print("\n--- Running ParseStaticDataNode (Second Run): Reading from cache ---")
    shared_cached = {"all_jobs": test_jobs_raw, "all_trainings": test_trainings_raw}
    parse_node_cached = ParseStaticDataNode()
    parse_node_cached.shared = shared_cached
    parse_node_cached.run(shared_cached)

    # Assert data was loaded from cache correctly
    assert len(shared_cached["parsed_jobs"]) == 5
    assert len(shared_cached["parsed_trainings"]) == 5
    assert shared_cached["parsed_jobs"][0].job_id == shared["parsed_jobs"][0].job_id

def test_load_static_data_node():
    node = LoadStaticDataNode()
    shared = {}
    node.run(shared)
    assert "all_jobs" in shared
    assert "all_trainings" in shared
    assert len(shared["all_jobs"]) == 200
    assert len(shared["all_trainings"]) == 497

@requires_aws_creds
@requires_mistral_key
def test_extract_profile_node_live():
    node = ExtractProfileNode()
    shared = {"persona_id": "persona_001"}
    node.run(shared)
    assert "persona_profile" in shared
    profile = shared["persona_profile"]
    assert isinstance(profile, PersonaProfile)

@pytest.mark.parametrize("profile_data, expected_action", [
    ({"age": 15, "goals": "find a job"}, "provide_awareness_young"),
    ({"age": 25, "goals": "I'm just exploring my options."}, "provide_awareness_info"),
    ({"age": 22, "goals": "I am not sure what I want yet."}, "provide_awareness_info"),
    ({"age": 30, "goals": "I want to learn new skills and get training."}, "recommend_trainings"),
    ({"age": 18, "goals": "Quero estudar e fazer cursos."}, "recommend_trainings"),
    ({"age": 28, "goals": "I need a job in the green sector."}, "recommend_jobs"),
    ({"age": 24, "goals": "I want to find a job and get training for it."}, "recommend_jobs"),
    ({"age": 40, "goals": "Looking for a new career."}, "recommend_jobs"),
])
def test_decision_node(profile_data, expected_action):
    node = DecisionNode()
    mock_profile = PersonaProfile(
        age=profile_data["age"],
        goals=profile_data["goals"],
        city="Test City",
        education_level="Ensino Médio",
        experience_years=2,
        skills=["testing"],
        is_open_to_relocate=False
    )
    shared = {"persona_profile": mock_profile}
    action = node.run(shared)
    assert shared["decision_action"] == expected_action
    assert action == expected_action

from src.nodes import ProvideAwarenessNode

@pytest.mark.parametrize("decision_action, expected_reason", [
    ("provide_awareness_young", "too_young"),
    ("provide_awareness_info", "info"),
])
def test_provide_awareness_node(decision_action, expected_reason):
    """
    Tests that the ProvideAwarenessNode correctly formats the output
    for both 'too_young' and 'info' scenarios.
    """
    # Arrange
    node = ProvideAwarenessNode()
    shared = {"decision_action": decision_action}

    # Act
    node.run(shared)

    # Assert
    assert "intermediate_recommendations" in shared
    recommendation = shared["intermediate_recommendations"]
    assert recommendation["predicted_type"] == "awareness"
    assert recommendation["predicted_items"] == expected_reason

from src.nodes import FindTrainingsOnlyNode

def test_find_trainings_only_node():
    """
    Tests that the FindTrainingsOnlyNode correctly identifies trainings
    that are the immediate next educational step for a persona.
    """
    # Arrange
    node = FindTrainingsOnlyNode()
    
    # Mock Persona with "Ensino Médio" (Level 2)
    mock_persona = PersonaProfile(
        age=20, city="Test", education_level="Ensino Médio",
        experience_years=1, skills=[], goals="learn", is_open_to_relocate=False
    )
    
    # Mock Trainings with various required levels
    # CORRECTED: Added 'offered_skills' to each mock profile
    mock_trainings = [
        TrainingProfile(training_id="tr1", title="Basic Course", offered_skills=["skill1"], required_level="Ensino Fundamental"), # Level 1 (too low)
        TrainingProfile(training_id="tr2", title="Technical Intro", offered_skills=["skill2"], required_level="Técnico"),         # Level 3 (correct)
        TrainingProfile(training_id="tr3", title="Another Tech", offered_skills=["skill3"], required_level="Técnico"),          # Level 3 (correct)
        TrainingProfile(training_id="tr4", title="Advanced Degree", offered_skills=["skill4"], required_level="Graduação"),      # Level 5 (too high)
        TrainingProfile(training_id="tr5", title="Master Class", offered_skills=["skill5"], required_level="Mestrado"),         # Level 7 (too high)
    ]
    
    shared = {
        "persona_profile": mock_persona,
        "parsed_trainings": mock_trainings
    }

    # Act
    node.run(shared)

    # Assert
    assert "intermediate_recommendations" in shared
    recommendation = shared["intermediate_recommendations"]
    assert recommendation["predicted_type"] == "trainings_only"
    
    recommended_ids = {t["training_id"] for t in recommendation["trainings"]}
    assert len(recommended_ids) == 2
    assert "tr2" in recommended_ids
    assert "tr3" in recommended_ids
    assert "tr1" not in recommended_ids # Should not recommend lower level
    assert "tr4" not in recommended_ids # Should not recommend level skipping