# Development Environment & Learning Approach

## Overview

This project serves a **dual purpose**: delivering a competition-ready solution for the Capgemini GDSC 2025 while acting as a **structured learning experience** in agentic AI development, LLM orchestration, and AWS cloud services. The development process is intentionally designed to be iterative, educational, and scalable.

---

## Development Environment: Amazon SageMaker

### Primary IDE: Amazon SageMaker Studio
- **Usage Model**: SageMaker will be used as a full-featured IDE for this project
- **Access**: AWS Sandbox Environment provided by the competition
- **Key Capabilities We'll Leverage**:
  - Jupyter notebooks for experimentation and visualization
  - Terminal access for command-line operations and testing
  - Integrated file management and module organization
  - Direct access to AWS services (S3, API endpoints)

---

## Learning-Focused Development Philosophy

### Core Principles

1. **Understand Before Automating**
   - Manually work through examples before building automated solutions
   - Document the "why" behind each design decision
   - Question assumptions and validate with data

2. **Incremental Complexity**
   - Start with the simplest working solution
   - Add complexity only when simpler approaches prove insufficient
   - Validate each increment before proceeding

3. **Terminal Proficiency as a Learning Goal**
   - Use terminal commands intentionally to build CLI fluency
   - Document useful commands in `docs/learning_log.md`
   - Balance terminal work with notebook-based visualization

4. **Test-Driven Learning**
   - Write tests to validate understanding, not just code correctness
   - Use failing tests as learning opportunities
   - Build a comprehensive test suite that documents expected behavior

---

## Development Workflow

### Phase 1: Setup & Exploration (Notebooks + Terminal)

```bash
# Terminal commands for initial setup
cd ./SageMaker
cd green-agent-age-of-inference-ii/
./run_start.sh # Bash script to setup the uv and git config
```

**Notebook Work:**
- `01_data_exploration.ipynb`: Load and analyze sample jobs, trainings
- Understand data schemas hands-on
- Visualize skill distributions, hard filter patterns

### Phase 2: Utility Development (Test-First Approach)

```bash
# Terminal-based test-driven development
uv run pytest -v -s tests/test_call_llm.py
```

**Development Pattern:**
1. Write test case in `tests/`
2. Run test (it fails)
3. Implement utility function
4. Run test (it passes)
5. Document in docstring with examples

**Notebook Work:**
- `04_llm_experiments.ipynb`: Test different prompts with Mistral
- Compare structured output formats (YAML vs JSON)
- Measure token usage for green optimization

### Phase 3: Node & Flow Implementation (Modular + Tested)

```bash
# Run specific node tests (just for example purpose)
pytest tests/test_nodes.py::TestPersonaAnalysisNode -v

# Test full flow integration (just for example purpose)
python src/main.py --persona-id pers_001 --dry-run
```

**Development Pattern:**
1. Design node in `docs/design.md` (high-level, no code)
2. Implement node in `src/nodes.py`
3. Write unit test in `tests/test_nodes.py`
4. Test with real data in notebook `02_matching_logic_tests.ipynb`

**Notebook Work:**
- `03_flow_visualization.ipynb`: Generate mermaid diagrams of flows
- Debug node interactions with detailed logging
- Profile execution time and token usage

### Phase 4: Integration & Optimization (Iterative Refinement)

```bash
# Run full evaluation on sample personas
uv run python src/main.py --mode evaluate --output results/eval_v1.json

# Compare with gold standard
uv run python scripts/compare_gold.py results/eval_v1.json data/gold_sample.json
```

**Notebook Work:**
- `05_evaluation.ipynb`: Analyze results vs gold standard
- Identify failure patterns
- Calculate green metrics (tokens/persona, API calls, latency)

---

## Learning Documentation

### Maintain a Learning Log (`docs/learning_log.md`)

Document discoveries as you go:

```markdown
## 2025-10-11: LLM Caching Strategy

**Challenge:** Node retries were returning cached results, causing validation failures.

**Solution:** Only use LLM cache when `self.cur_retry == 0` in Node.exec()

**Code Pattern:**
```python
use_cache = self.cur_retry == 0
response = call_llm(prompt, use_cache=use_cache)
```

**Learning:** PocketFlow's retry mechanism needs cache-aware implementations.

---

## Notebook Usage Guidelines

### When to Use Notebooks
- **Data exploration**: Understanding schemas and distributions
- **Visualization**: Mermaid diagrams, metrics charts, flow debugging
- **Experimentation**: Prompt engineering, parameter tuning
- **Analysis**: Comparing results, error pattern analysis

### When to Use Terminal/Scripts
- **Running tests**: `pytest` for all unit and integration tests
- **Deployment**: Executing the full system on multiple personas
- **Automation**: Batch processing, scheduled tasks
- **Version control**: All git operations

### Best Practice: Notebook → Module Pattern
1. Prototype logic in a notebook cell
2. Once working, refactor into a module (`.py` file)
3. Import module into notebook for continued experimentation
4. Write tests for the module

**Example:**
```python
# In notebook: 02_matching_logic_tests.ipynb
from src.utils.matching import apply_hard_filters, calculate_skill_coverage

# Test with sample data
persona = {...}
job = {...}
result = apply_hard_filters(persona, job)
print(f"Passes filters: {result}")
```

---

## Green Solution: Resource Optimization Tracking

### Metrics to Monitor

Track in `05_evaluation.ipynb`:

```python
metrics = {
    'avg_tokens_per_persona': [],
    'avg_llm_calls_per_persona': [],
    'avg_latency_seconds': [],
    'cache_hit_rate': []
}
```

### Optimization Techniques

1. **Prompt Compression**: Remove unnecessary verbosity
2. **Strategic Caching**: Cache persona analysis results
3. **Batch Operations**: Group similar LLM calls
4. **Early Filtering**: Apply hard filters before LLM reasoning
5. **Lazy Loading**: Only fetch data when needed

---

## Scalability Considerations

### Design for Growth
- **Modular architecture**: Each component can be scaled independently
- **Stateless nodes**: Enable horizontal scaling
- **Async operations**: Prepare for parallel processing
- **Configuration-driven**: Easy to adjust without code changes

### From Learning Project to Production
- Clean separation of concerns (utils, nodes, flows)
- Comprehensive test coverage
- Documented design decisions
- Monitored performance metrics

This structure allows the project to serve both as a learning vehicle and a competition-ready solution.

---

## Integration with AI Coding Instructions

Existing `docs/ai_coding_instructions.md` should be referenced throughout development:

The AI assistant should treat both this document and `ai_coding_instructions.md` as authoritative guides for development decisions.

---