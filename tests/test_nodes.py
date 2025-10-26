import pytest
import os
import json
import getpass
from src.nodes import LoadStaticDataNode, ExtractProfileNode, PersonaProfile
from dotenv import load_dotenv

# --- Load .env file for MISTRAL_API_KEY ---
load_dotenv()

# --- Interactive Credential Setup ---
# Helper function to prompt for credentials if they are not found.
def setup_credentials():
    """Checks for necessary API keys and prompts the user if they are missing."""
    creds_to_check = {
        "MISTRAL_API_KEY": "Enter your Mistral API Key: ",
        "AWS_ACCESS_KEY_ID": "Enter your AWS Access Key ID: ",
        "AWS_SECRET_ACCESS_KEY": "Enter your AWS Secret Access Key: ",
        "AWS_SESSION_TOKEN": "Enter your AWS Session Token: "
    }
    
    for key, prompt_text in creds_to_check.items():
        if not os.getenv(key):
            print(f"Environment variable '{key}' not found.")
            # Use getpass for secret keys to hide input
            if "KEY" in key or "TOKEN" in key:
                value = getpass.getpass(prompt_text)
            else:
                value = input(prompt_text)
            os.environ[key] = value
            print(f"✅ '{key}' set for this session.")

# Run the setup function when the test module is loaded.
setup_credentials()

# --- Reusable Pytest Marker ---
# This defines the marker that was missing before.
# It skips tests if essential AWS credentials for the GDSC API are not set.
requires_aws_creds = pytest.mark.skipif(
    not os.getenv("AWS_ACCESS_KEY_ID") or not os.getenv("AWS_SECRET_ACCESS_KEY"),
    reason="This test makes a live API call and requires AWS credentials."
)


def test_load_static_data_node():
    """

    Tests that the LoadStaticDataNode correctly loads jobs and trainings
    and populates the shared store.
    """
    # Arrange
    node = LoadStaticDataNode()
    shared = {}

    # Act
    node.run(shared)

    # Assert
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
    """
    A live integration test for the ExtractProfileNode.
    It calls the actual GDSC API to chat with a persona and then uses
    a real LLM call to extract and validate the profile using Pydantic.
    """
    # Arrange
    node = ExtractProfileNode()
    shared = {"persona_id": "persona_001"}

    # Act
    node.run(shared)

    # Assert
    assert "persona_profile" in shared
    assert "conversation_id" in shared
    assert "conversation_history" in shared

    # Assert profile is a Pydantic model instance
    profile = shared["persona_profile"]
    assert isinstance(profile, PersonaProfile)
    
    # Assert specific fields for type safety
    assert isinstance(profile.age, int)
    assert isinstance(profile.city, str)
    assert len(profile.city) > 0

    # Assert conversation details
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