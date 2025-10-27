import pytest
import os
import json
import getpass
from pathlib import Path
from src.nodes import LoadStaticDataNode, ExtractProfileNode, DecisionNode, ParseStaticDataNode, PersonaProfile, JobProfile, TrainingProfile
from src.utils.matching_rules import EDUCATION_LEVELS
from dotenv import load_dotenv
from src.utils.gdsc_utils import sanity_check

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

# --- Helper function for credential checking ---
def check_and_get_aws_credentials():
    """Checks for AWS credentials, prompts if necessary, and returns True if ready."""
    if all(os.getenv(key) for key in ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]):
        print("\n✅ AWS credentials found in environment.")
        return True

    print("\n🔑 AWS Credential Check")
    is_interactive = os.isatty(0)
    
    if is_interactive:
        response = input("Are you in an environment with an IAM role (e.g., SageMaker)? [y/n]: ").lower()
    else:
        print("Non-interactive environment detected. Assuming IAM role.")
        response = 'y'

    if response == 'y':
        print("Proceeding with IAM role-based authentication.")
        try:
            if not sanity_check(verbose=False):
                print("⚠️ Warning: Sanity check to AWS failed with IAM role.")
        except Exception as e:
            print(f"⚠️ Warning: Sanity check to AWS failed: {e}")
        return True # Assume role is present and let the API call try
    else:
        print("🔧 Please provide temporary AWS credentials.")
        # Using getpass to hide secret key input
        key_id = input("Enter AWS Access Key ID: ")
        secret_key = getpass.getpass("Enter AWS Secret Access Key: ")
        token = getpass.getpass("Enter AWS Session Token: ")
        if not all([key_id, secret_key, token]):
            print("❌ Incomplete credentials provided.")
            return False
        os.environ["AWS_ACCESS_KEY_ID"] = key_id
        os.environ["AWS_SECRET_ACCESS_KEY"] = secret_key
        os.environ["AWS_SESSION_TOKEN"] = token
        print("✅ Manual credentials set for this session.")
        return True

@requires_mistral_key # We still need the Mistral key
def test_extract_profile_node_dynamic_live():
    """
    Performs a live, end-to-end test of the dynamic ExtractProfileNode.
    It now interactively checks for credentials and allows persona selection.
    """
    # 1. Credential Check
    if not check_and_get_aws_credentials():
        pytest.skip("AWS credentials were not provided. Skipping live test.")

    # 2. Persona Selection
    persona_num_str = input("\nEnter a persona number to test (1-100): ")
    try:
        persona_num = int(persona_num_str)
        if not 1 <= persona_num <= 100:
            raise ValueError
        persona_to_test = f"persona_{persona_num:03d}"
    except (ValueError, TypeError):
        default_persona = "persona_001"
        print(f"Invalid input. Defaulting to {default_persona}.")
        persona_to_test = default_persona
    
    # 3. Arrange
    node = ExtractProfileNode()
    shared = {"persona_id": persona_to_test}
    
    print(f"\n--- Starting LIVE dynamic conversation test for {persona_to_test} ---")

    # 4. Act
    node.run(shared)

    # 5. Assert
    assert "persona_profile" in shared
    profile = shared["persona_profile"]
    assert isinstance(profile, PersonaProfile)
    
    assert "conversation_history" in shared
    assert len(shared["conversation_history"]) > 0
    
    print(f"\n--- Live Test Complete for {persona_to_test} ---")
    print("Final Extracted Profile:")
    print(profile.model_dump_json(indent=2))
    print("\nConversation History:")
    for turn in shared["conversation_history"]:
        print(f"  Q: {turn['question']}")
        print(f"  A: {turn['answer']}")

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
    that are the immediate next step OR are open to all levels.
    """
    # Arrange
    node = FindTrainingsOnlyNode()
    
    mock_persona = PersonaProfile(
        age=20, city="Test", education_level="Ensino Médio", # Level 2
        experience_years=1, skills=[], goals="learn", is_open_to_relocate=False
    )
    
    # CORRECTED: Added 'offered_skills' to each mock profile
    mock_trainings = [
        TrainingProfile(training_id="tr1", title="Basic Course", offered_skills=["skill1"], required_level="Ensino Fundamental"), # Level 1 (too low)
        TrainingProfile(training_id="tr2", title="Technical Intro", offered_skills=["skill2"], required_level="Técnico"),         # Level 3 (correct next step)
        TrainingProfile(training_id="tr3", title="Another Tech", offered_skills=["skill3"], required_level="Técnico"),          # Level 3 (correct next step)
        TrainingProfile(training_id="tr4", title="Advanced Degree", offered_skills=["skill4"], required_level="Graduação"),      # Level 5 (too high)
        TrainingProfile(training_id="tr5", title="Open for All", offered_skills=["skill5"], required_level=None),               # Level 0 (correct, open)
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
    
    recommended_ids = {t["training_id"] for t in recommendation["trainings"]}
    assert len(recommended_ids) == 3
    assert "tr2" in recommended_ids # Next level
    assert "tr3" in recommended_ids # Next level
    assert "tr5" in recommended_ids # Open to all
    assert "tr1" not in recommended_ids
    assert "tr4" not in recommended_ids

from src.nodes import FindJobsAndTrainingsNode

def test_find_jobs_and_trainings_node():
    """
    Tests the full logic of the FindJobsAndTrainingsNode:
    1. It correctly filters jobs.
    2. It correctly identifies skill gaps.
    3. It correctly recommends trainings for those gaps.
    """
    # Arrange
    node = FindJobsAndTrainingsNode()
    
    # Mock Persona
    mock_persona = PersonaProfile(
        age=25, city="São Paulo", education_level="Graduação", experience_years=3,
        skills=["Python", "SQL"], languages=["Portuguese", "English"],
        goals="find a job", is_open_to_relocate=False
    )

    # Mock Jobs
    mock_jobs = [
        # Passes filters, but needs 'Data Visualization' skill
        JobProfile(job_id="j1", title="Data Analyst", city="São Paulo", is_remote=False,
                   education_level="Graduação", experience_years=2, languages=["Portuguese"],
                   required_skills=["Python", "SQL", "Data Visualization"]),
        # Perfect match, no missing skills
        JobProfile(job_id="j2", title="Backend Dev", city="São Paulo", is_remote=True,
                   education_level="Técnico", experience_years=3, languages=["English"],
                   required_skills=["Python"]),
        # Fails location filter
        JobProfile(job_id="j3", title="Manager", city="Recife", is_remote=False,
                   education_level="Graduação", experience_years=3, languages=["Portuguese"],
                   required_skills=["Management"]),
        # Fails experience filter
        JobProfile(job_id="j4", title="Senior Analyst", city="São Paulo", is_remote=False,
                   education_level="Graduação", experience_years=5, languages=["Portuguese"],
                   required_skills=["Python"]),
    ]
    
    # Mock Trainings
    mock_trainings = [
        TrainingProfile(training_id="tr10", title="Intro to Viz", offered_skills=["Data Visualization", "BI Tools"]),
        TrainingProfile(training_id="tr11", title="Advanced Viz", offered_skills=["Data Visualization", "Tableau"]),
        TrainingProfile(training_id="tr12", title="Other Skill", offered_skills=["Project Management"]),
    ]

    shared = {
        "persona_profile": mock_persona,
        "parsed_jobs": mock_jobs,
        "parsed_trainings": mock_trainings
    }

    # Act
    node.run(shared)

    # Assert
    assert "intermediate_recommendations" in shared
    recs = shared["intermediate_recommendations"]
    assert recs["predicted_type"] == "jobs+trainings"
    assert len(recs["jobs"]) == 2  # j3 and j4 should be filtered out

    # Find the recommendations for j1 and j2
    rec_j1 = next((j for j in recs["jobs"] if j["job_id"] == "j1"), None)
    rec_j2 = next((j for j in recs["jobs"] if j["job_id"] == "j2"), None)
    
    # Assertions for j1 (has skill gap)
    assert rec_j1 is not None
    assert len(rec_j1["suggested_trainings"]) == 1
    skill_gap = rec_j1["suggested_trainings"][0]
    # CORRECTED: Assert against the lowercase version
    assert skill_gap["missing_skill"] == "data visualization"
    recommended_training_ids = {t["training_id"] for t in skill_gap["trainings"]}
    assert recommended_training_ids == {"tr10", "tr11"}

    # Assertions for j2 (perfect match)
    assert rec_j2 is not None
    assert len(rec_j2["suggested_trainings"]) == 0

from src.nodes import FinalizeOutputNode

@pytest.mark.parametrize("intermediate_recs", [
    # Case 1: Awareness
    ({"predicted_type": "awareness", "predicted_items": "too_young"}),
    # Case 2: Trainings Only
    ({"predicted_type": "trainings_only", "trainings": [{"training_id": "tr1"}]}),
    # Case 3: Jobs + Trainings
    ({"predicted_type": "jobs+trainings", "jobs": [{"job_id": "j1", "suggested_trainings": []}]}),
])
def test_finalize_output_node(intermediate_recs):
    """
    Tests that the FinalizeOutputNode correctly merges the persona_id
    with the recommendation payload from any of the logic branches.
    """
    # Arrange
    node = FinalizeOutputNode()
    shared = {
        "persona_id": "persona_test_123",
        "intermediate_recommendations": intermediate_recs
    }

    # Act
    node.run(shared)

    # Assert
    assert "final_recommendation" in shared
    final_rec = shared["final_recommendation"]

    # Check that persona_id is present and correct
    assert "persona_id" in final_rec
    assert final_rec["persona_id"] == "persona_test_123"

    # Check that all keys from the intermediate recs are present
    for key, value in intermediate_recs.items():
        assert key in final_rec
        assert final_rec[key] == value