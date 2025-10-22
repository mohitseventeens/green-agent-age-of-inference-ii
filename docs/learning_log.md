# Learning Log

## 2025-10-22: Initial Design & Core LLM Utility

**Progress:**
- **Phase 1 (Design):** Successfully completed the high-level design phase.
    - Created a comprehensive `docs/design.md` file that outlines the entire system architecture, from requirements and user stories to the specific design of the `shared` store and each `Node`.
    - Clarified that job/training data is available locally as markdown files.
    - Confirmed that the `gdsc_utils` are optional helpers we can leverage.
- **Phase 2 (Utilities):** Began implementation of core utilities.
    - Implemented the first version of `src/utils/call_llm.py` to connect with the Mistral API.
    - Implemented a robust caching strategy (`@lru_cache`) that respects the `use_cache` flag, which is crucial for handling node retries correctly as per the Agentic Coding guide.
    - Created the initial `pytest` file `tests/test_call_llm.py` to formalize testing.

**Key Learnings & Challenges:**
- **Serialization for Caching:** The initial implementation of `call_llm.py` failed because the `messages` list was converted to a `tuple` to be hashable for caching, but the Mistral client's Pydantic validator couldn't parse this tuple format.
- **FAIL FAST Principle:** The error was caught immediately by running the script's `if __name__ == '__main__':` block. This prevented a more complex debugging session later.
- **Resolution:** The fix was to ensure the `messages` payload was correctly reconstructed back into a `list` of `dict`s before being passed to the Mistral client.
- **Dependency Management:** Attempting to run the pytest file directly revealed that `pytest` was not yet installed in the `uv` environment. This highlights the importance of explicitly managing development dependencies.

**Decisions Made:**
- The system will use a rule-based `DecisionNode` for initial path selection (`jobs`, `trainings`, `awareness`). This is a "Green" decision to conserve LLM tokens by avoiding unnecessary API calls for simple classification tasks.
- The `pytest` framework will be used for all formal testing. Tests requiring API keys will be marked to be skipped in environments where keys are not present.

**Next Steps:**
- Install `pytest` and run the formal tests for `call_llm.py`.
- Implement the next utility: `src/utils/data_retrieval.py`.