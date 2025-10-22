# Terminal Training Log

This log captures commands, outputs, and key terminal sessions for learning and debugging purposes.

---

### Session: 2025-10-21 - Implementing and Debugging `call_llm.py`

**Goal:** Implement the Mistral API utility and test it.

**Command 1: Initial Run (Failure)**
```sh
sh-4.2$ uv run src/utils/call_llm.py 
2025-10-21 14:21:53,460 - __main__ - INFO - Loaded environment variables from: /home/ec2-user/SageMaker/green-agent-age-of-inference-ii/src/utils/../../.env
2025-10-21 14:21:53,460 - __main__ - INFO - --- Running Self-Test for call_llm utility ---

--- Test 1: First call (no cache) ---
2025-10-21 14:21:53,460 - __main__ - INFO - Cache is disabled. Forcing a fresh API call...
2025-10-21 14:21:53,542 - __main__ - INFO - Making a LIVE API call to model: mistral-small-latest...
2025-10-21 14:21:53,554 - __main__ - ERROR - Mistral API call failed: Could not find discriminator field role in (('role', 'user'), ('content', "What is a 'green job' in Brazil? Keep it short and practical."))
Traceback (most recent call last):
  File "/home/ec2-user/SageMaker/green-agent-age-of-inference-ii/src/utils/call_llm.py", line 83, in call_llm
    return _cached_mistral_call.__wrapped__(model, messages_tuple)
...
ValueError: Could not find discriminator field role in (('role', 'user'), ('content', "What is a 'green job' in Brazil? Keep it short and practical."))
```
**Observation:** The script failed with a `ValueError`. The Mistral client did not accept the `tuple` format used for caching.

---

**Action:** Corrected the `_cached_mistral_call` function in `src/utils/call_llm.py` to reconstruct the `list` of `dict`s from the `tuple` before making the API call.

---

**Command 2: Second Run (Success)**
```sh
sh-4.2$ uv run src/utils/call_llm.py 
2025-10-21 14:27:36,188 - __main__ - INFO - Loaded environment variables from: /home/ec2-user/SageMaker/green-agent-age-of-inference-ii/src/utils/../../.env
2025-10-21 14:27:36,188 - __main__ - INFO - --- Running Self-Test for call_llm utility ---

--- Test 1: First call (cache enabled, but no entry exists) ---
2025-10-21 14:27:36,188 - __main__ - INFO - Cache is enabled. Checking for a cached response...
2025-10-21 14:27:36,273 - __main__ - INFO - Making a LIVE API call to model: mistral-small-latest...
Response 1:
In Brazil, a **green job** is a position that contributes to environmental sustainability...

--- Test 2: Second call (with cache, should be a HIT) ---
2025-10-21 14:27:42,250 - __main__ - INFO - Cache is enabled. Checking for a cached response...
Response 2:
In Brazil, a **green job** is a position that contributes to environmental sustainability...

--- Test 3: Third call (no cache again) ---
2025-10-21 14:27:42,250 - __main__ - INFO - Cache is disabled. Forcing a fresh API call...
2025-10-21 14:27:42,269 - __main__ - INFO - Making a LIVE API call to model: mistral-small-latest...
Response 3:
A **green job** in Brazil is a position that contributes to environmental sustainability...

--- Self-Test Complete ---
```
**Observation:** The fix worked. The self-test now passes, and the caching logic is confirmed to be functioning correctly.

---

**Command 3: Attempt to Run Pytest (Failure)**
```sh
sh-4.2$ uv run tests/test_call_llm.py 
Traceback (most recent call last):
  File "/home/ec2-user/SageMaker/green-agent-age-of-inference-ii/tests/test_call_llm.py", line 1, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'
```
**Observation:** The command failed because `pytest` is a test runner, not a script to be executed directly, and the module was not installed in the virtual environment.

---