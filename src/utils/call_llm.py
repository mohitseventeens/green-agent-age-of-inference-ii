# MODIFIED: src/utils/call_llm.py

import os
import logging
from functools import lru_cache
from mistralai import Mistral
from typing import List, Dict, Optional, Tuple

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
# (logging setup code remains the same as before)
if not logger.handlers:
    logger.setLevel(logging.WARNING)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# --- Global cost tracker for the entire run ---
# This dictionary will be imported and used by main.py
COST_TRACKER = {
    'total_cost': 0.0,
    'by_model': {}
}

MISTRAL_PRICING = {
    'mistral-large-latest': {'input': 2.00, 'output': 6.00},  # per 1M tokens
    'mistral-medium-latest': {'input': 0.40, 'output': 2.00}, # per 1M tokens
    'mistral-small-latest': {'input': 0.10, 'output': 0.30},  # per 1M tokens
}

# --- Internal cached function ---
@lru_cache(maxsize=256) # Increased cache size
def _cached_mistral_call(model: str, messages_tuple: tuple) -> Tuple[str, int, int]:
    """
    Internal function that performs the actual API call and returns token usage.
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY environment variable not found.")
        
    client = Mistral(api_key=api_key)
    messages_list = [dict(msg_tuple) for msg_tuple in messages_tuple]
    
    logger.info(f"Making a LIVE API call to model: {model}...")
    response = client.chat.complete(
        model=model,
        messages=messages_list
    )
    
    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens
    
    return response.choices[0].message.content, input_tokens, output_tokens

# --- Main utility function for external use ---
def call_llm(
    prompt: Optional[str] = None,
    messages: Optional[List[Dict[str, str]]] = None,
    model: str = "mistral-small-latest",
    use_cache: bool = True
) -> str:
    """
    Wrapper for Mistral API calls that also tracks cost and token usage.
    Now it only returns the string content for backward compatibility with nodes.
    Cost tracking happens globally.
    """
    if prompt:
        messages_payload = [{"role": "user", "content": prompt}]
    elif messages:
        messages_payload = messages
    else:
        raise ValueError("You must provide either a 'prompt' or 'messages'.")

    try:
        messages_tuple = tuple(tuple(item.items()) for item in messages_payload)
        
        is_cache_hit = _cached_mistral_call.cache_info().hits > 0 if use_cache else False

        if use_cache:
            content, input_tokens, output_tokens = _cached_mistral_call(model, messages_tuple)
        else:
            # Bypass cache for a fresh call
            content, input_tokens, output_tokens = _cached_mistral_call.__wrapped__(model, messages_tuple)
        
        # --- Cost Tracking Logic ---
        if not (use_cache and is_cache_hit): # Only track cost for non-cached calls
            pricing = MISTRAL_PRICING.get(model, {'input': 0, 'output': 0})
            input_cost = (input_tokens / 1_000_000) * pricing['input']
            output_cost = (output_tokens / 1_000_000) * pricing['output']
            call_cost = input_cost + output_cost

            COST_TRACKER['total_cost'] += call_cost
            if model not in COST_TRACKER['by_model']:
                COST_TRACKER['by_model'][model] = {'calls': 0, 'input_tokens': 0, 'output_tokens': 0, 'cost': 0.0}
            
            COST_TRACKER['by_model'][model]['calls'] += 1
            COST_TRACKER['by_model'][model]['input_tokens'] += input_tokens
            COST_TRACKER['by_model'][model]['output_tokens'] += output_tokens
            COST_TRACKER['by_model'][model]['cost'] += call_cost
            
        return content
            
    except Exception as e:
        logger.error(f"Mistral API call failed: {e}", exc_info=True)
        raise