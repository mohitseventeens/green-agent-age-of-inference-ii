import pytest
import os
import json
import getpass
from src.nodes import LoadStaticDataNode, ExtractProfileNode, DecisionNode, PersonaProfile
from dotenv import load_dotenv

# --- Load .env file for MISTRAL_API_KEY ---
load_dotenv()

# --- Interactive Credential Setup ---
def setup_credentials():
    creds_to_check = {
        "MISTRAL_API_KEY": "Enter your Mistral API Key: ",
        "AWS_ACCESS_KEY_ID": "Enter your AWS Access Key ID: ",
        "AWS_SECRET_ACCESS_KEY": "Enter your AWS Secret Access Key: ",
        "AWS_SESSION_TOKEN": "Enter your AWS Session Token: "
    }
    
    for key, prompt_text in creds_to_check.items():
        if not os.getenv(key):
            print(f"Environment variable '{key}' not found.")
            if "KEY" in key or "TOKEN" in key:
                value = getpass.getpass(prompt_text)
            else:
                value = input(prompt_text)
            os.environ[key] = value
            print(f"✅ '{key}' set for this session.")

setup_credentials()

requires_aws_creds = pytest.mark.skipif(
    not os.getenv("AWS_ACCESS_KEY_ID") or not os.getenv("AWS_SECRET_ACCESS_KEY"),
    reason="This test makes a live API call and requires AWS credentials."
)


def test_load_static_data_node():
    node = LoadStaticDataNode()
    shared = {}
    node.run(shared)
    assert "all_jobs" in shared
    assert "all_trainings" in shared
    assert isinstance(shared["all_jobs"], list)
    assert len(shared["all_jobs"]) == 200
    assert isinstance(shared["all_trainings"], list)
    assert len(shared["all_trainings"]) == 497
    assert shared["all_jobs"][0]["id"] == "j0"
    assert shared["all_trainings"][0]["id"] == "tr0"


@requires_aws_creds
def test_extract_profile_node_live():
    node = ExtractProfileNode()
    shared = {"persona_id": "persona_001"}
    node.run(shared)
    assert "persona_profile" in shared
    assert "conversation_id" in shared
    assert "conversation_history" in shared
    profile = shared["persona_profile"]
    assert isinstance(profile, PersonaProfile)
    assert isinstance(profile.age, int)
    assert isinstance(profile.city, str)
    assert len(profile.city) > 0
    assert isinstance(shared["conversation_id"], str)
    assert len(shared["conversation_id"]) > 10
    assert isinstance(shared["conversation_history"], list)
    assert len(shared["conversation_history"]) == 3
    print("\n--- Live Test: ExtractProfileNode ---")
    print(f"Persona ID: {shared['persona_id']}")
    print(f"Conversation ID: {shared['conversation_id']}")
    print(f"Profile Object Type: {type(profile)}")
    print("Extracted Profile (Validated):")
    print(json.dumps(profile.model_dump(), indent=2, ensure_ascii=False))
    print("--- Test Passed ---")


# --- Unit Tests for DecisionNode ---
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
    """
    Tests the DecisionNode logic across all defined branches using mocked profiles.
    """
    # Arrange
    node = DecisionNode()
    # Create a mock profile, filling in required fields with dummy data
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

    # Act
    action = node.run(shared)

    # Assert
    assert shared["decision_action"] == expected_action
    assert action == expected_action
    print(f"Tested goals: '{profile_data['goals']}' -> PASSED with action: '{action}'")