import os
import logging
from functools import lru_cache
from mistralai import Mistral
from typing import List, Dict, Optional

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- Internal cached function ---
@lru_cache(maxsize=128)
def _cached_mistral_call(model: str, messages_tuple: tuple) -> str:
    """
    Internal function that performs the actual API call.
    Caching is applied here. Messages are converted to a tuple to be hashable.
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        logger.error("Cannot call Mistral API, MISTRAL_API_KEY is not set.")
        raise ValueError("MISTRAL_API_KEY environment variable not found.")
        
    client = Mistral(api_key=api_key)
    
    # --- FIX: Correctly reconstruct the list of dictionaries from the tuple ---
    # The input `messages_tuple` looks like: ((('role', 'user'), ('content', '...')),)
    # We need to convert it back to: [{'role': 'user', 'content': '...'}]
    messages_list = [dict(msg_tuple) for msg_tuple in messages_tuple]
    # --------------------------------------------------------------------------
    
    logger.info(f"Making a LIVE API call to model: {model}...")
    response = client.chat.complete(
        model=model,
        messages=messages_list
    )
    return response.choices[0].message.content

# --- Main utility function for external use ---
def call_llm(
    prompt: Optional[str] = None,
    messages: Optional[List[Dict[str, str]]] = None,
    model: str = "mistral-small-latest",
    use_cache: bool = True
) -> str:
    """
    A robust wrapper for making calls to the Mistral API.

    This function handles chat history, caching, and retries as per Agentic Coding guidelines.

    Args:
        prompt (Optional[str]): A single user prompt. If provided, it overrides `messages`.
        messages (Optional[List[Dict[str, str]]]): A list of messages for chat history.
        model (str): The Mistral model to use. Defaults to "mistral-small-latest".
        use_cache (bool): If True, returns a cached result for the same request.
                          Should be set to `self.cur_retry == 0` within a PocketFlow Node's
                          `exec` method to avoid getting stale results on retries.

    Returns:
        str: The content of the LLM's response.
    
    Raises:
        ValueError: If neither `prompt` nor `messages` are provided, or if the API key is missing.
    """
    if prompt:
        messages_payload = [{"role": "user", "content": prompt}]
    elif messages:
        messages_payload = messages
    else:
        raise ValueError("You must provide either a 'prompt' or 'messages'.")

    try:
        # Convert the list of dictionaries to a tuple of tuples of items to make it hashable
        messages_tuple = tuple(tuple(item.items()) for item in messages_payload)
        
        if use_cache:
            logger.info("Cache is enabled. Checking for a cached response...")
            return _cached_mistral_call(model, messages_tuple)
        else:
            logger.info("Cache is disabled. Forcing a fresh API call...")
            # Use __wrapped__ to bypass the cache of the decorated function
            return _cached_mistral_call.__wrapped__(model, messages_tuple)
            
    except Exception as e:
        logger.error(f"Mistral API call failed: {e}", exc_info=True)
        # Re-raise the exception so the caller (e.g., a PocketFlow Node) can handle it
        raise

# --- Self-testing block ---
if __name__ == '__main__':
    # Ensure you have a .env file with MISTRAL_API_KEY in the project root
    from dotenv import load_dotenv
    env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
        logger.info(f"Loaded environment variables from: {env_path}")

    if not os.getenv("MISTRAL_API_KEY"):
        logger.error("FATAL: MISTRAL_API_KEY not found. Please create a .env file in the project root.")
    else:
        logger.info("--- Running Self-Test for call_llm utility ---")
        test_prompt = "What is a 'green job' in Brazil? Keep it short and practical."

        # 1. First call - should be a LIVE call
        print("\n--- Test 1: First call (cache enabled, but no entry exists) ---")
        response1 = call_llm(prompt=test_prompt, use_cache=True)
        print(f"Response 1:\n{response1}")

        # 2. Second call with cache enabled - should be INSTANT and cached
        print("\n--- Test 2: Second call (with cache, should be a HIT) ---")
        response2 = call_llm(prompt=test_prompt, use_cache=True)
        print(f"Response 2:\n{response2}")
        
        # 3. Third call with same prompt but cache disabled - should be a LIVE call again
        print("\n--- Test 3: Third call (no cache again) ---")
        response3 = call_llm(prompt=test_prompt, use_cache=False)
        print(f"Response 3:\n{response3}")

        print("\n--- Self-Test Complete ---")