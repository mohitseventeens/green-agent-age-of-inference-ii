import pytest
import os
from dotenv import load_dotenv
from src.utils.call_llm import CallMistral

# Load environment variables from a .env file if it exists
# This is great for local development and ensures the test can find the API key
load_dotenv()

# Decorator to skip this test if the API key isn't available in the environment.
# This prevents test failures in CI/CD or other secure environments.
@pytest.mark.skipif(not os.environ.get("MISTRAL_API_KEY"), reason="MISTRAL_API_KEY environment variable not set")
def test_call_mistral_node_real_api_call():
    """
    Tests the CallMistral node by making a real API call to the Mistral service.
    This serves as an integration test to ensure compatibility with the live API.
    """
    # 1. Initialize the node
    # Use a single attempt for testing to get faster feedback
    node = CallMistral(max_retries=1)

    # 2. Set the parameters for the API call
    node.set_params({
        "model": "mistral-small-latest",
        "messages": [{"role": "user", "content": "What is the capital of France? Respond with only the name."}]
    })

    # 3. Execute the node's full lifecycle
    result = node.run(shared={})

    # 4. Print the result for easy debugging during the test run
    print(f"\n--- Real API Call Result ---\nResponse: {result}\n--------------------------")

    # 5. Assertions
    # Check that the result is a string and is not empty.
    assert isinstance(result, str)
    assert len(result) > 0
    # Check that the response contains the expected answer.
    assert "Paris" in result