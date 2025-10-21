import pytest
import os
from src.utils.call_llm import call_llm
from dotenv import load_dotenv

_ = load_dotenv()

# --- Marker to check if the MISTRAL_API_KEY is available ---
# The test will be skipped if the API key is not found in the environment variables.
# This prevents test failures in CI/CD or other environments without the key.
requires_mistral_api_key = pytest.mark.skipif(
    not os.getenv("MISTRAL_API_KEY"),
    reason="This test requires the MISTRAL_API_KEY environment variable to be set."
)

@requires_mistral_api_key
def test_call_llm_with_api_key_returns_string_response():
    """
    Tests that a call to the Mistral API with a valid key and prompt
    returns a non-empty string response.
    
    This test makes a real, live API call.
    """
    # Arrange
    test_prompt = "What are the three most common renewable energy sources?"
    
    # Act
    # We call with use_cache=False to ensure the test always hits the live API
    response = call_llm(prompt=test_prompt, use_cache=False)
    
    # Assert
    assert isinstance(response, str), "The response should be a string."
    assert len(response) > 0, "The response string should not be empty."
    print(f"Response: \n{response}\n")
    print(f"\nLive API test successful. Received response of {len(response)} characters.")

def test_call_llm_without_prompt_or_messages_raises_error():
    """
    Tests that the call_llm function raises a ValueError if no input is provided.
    """
    # Arrange, Act, Assert
    with pytest.raises(ValueError, match="You must provide either a 'prompt' or 'messages'."):
        call_llm()

def test_call_llm_without_api_key_raises_error(monkeypatch):
    """
    Tests that the call_llm function raises a ValueError if the API key is missing.
    We use monkeypatch to temporarily remove the environment variable for this test.
    """
    # Arrange
    # Temporarily remove the API key from the environment for the duration of this test
    if "MISTRAL_API_KEY" in os.environ:
        monkeypatch.delenv("MISTRAL_API_KEY")
    
    test_prompt = "This should fail."
    
    # Act, Assert
    with pytest.raises(ValueError, match="MISTRAL_API_KEY environment variable not found."):
        call_llm(prompt=test_prompt)