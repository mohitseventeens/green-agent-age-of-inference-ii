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

### Development Structure

```
sagemaker-workspace/
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Explore persona/job/training data
│   ├── 02_matching_logic_tests.ipynb  # Test matching rules iteratively
│   ├── 03_flow_visualization.ipynb    # Visualize agent flows with mermaid
│   ├── 04_llm_experiments.ipynb       # Prompt engineering experiments
│   └── 05_evaluation.ipynb            # Results analysis and metrics
├── src/
│   ├── __init__.py
│   ├── main.py                        # Entry point for the system
│   ├── nodes.py                       # PocketFlow node implementations
│   ├── flow.py                        # Flow orchestration logic
│   └── utils/
│       ├── __init__.py
│       ├── call_llm.py               # Mistral API wrapper
│       ├── data_retrieval.py         # data fetching
│       ├── embedding.py              # Embedding generation (if RAG)
│       ├── matching.py               # Hard filter & skill coverage logic
│       └── validation.py             # Output validation utilities
├── tests/
│   ├── test_utils.py                 # Unit tests for utilities
│   ├── test_nodes.py                 # Unit tests for nodes
│   ├── test_matching.py              # Tests for matching logic
│   └── test_integration.py           # End-to-end flow tests
├── data/
│   ├── jobs/                         # 200 Job description markdown files
│   └── trainings/                    # 497 training markdown files
├── docs/
│   ├── development_environment.md                # The current document
│   ├── design.md                     # High-level system design
│   ├── ai_coding_instructions.md     # AI coding guide
│   └── learning_log.md               # Document insights and learnings
│   └── terminal_training.md          # Learning through Practice
├── requirements.txt
└── README.md
```

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
```

**Notebook Work:**
- `01_data_exploration.ipynb`: Load and analyze sample personas, jobs, trainings
- Understand data schemas hands-on
- Visualize skill distributions, hard filter patterns

### Phase 2: Utility Development (Test-First Approach)

```bash
# Terminal-based test-driven development
pytest tests/test_utils.py -v
pytest tests/test_matching.py -v --cov=src/utils
```

**Development Pattern:**
1. Write test case in `tests/test_utils.py`
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
# Run specific node tests
pytest tests/test_nodes.py::TestPersonaAnalysisNode -v

# Test full flow integration
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
python src/main.py --mode evaluate --output results/eval_v1.json

# Compare with gold standard
python scripts/compare_gold.py results/eval_v1.json data/gold_sample.json
```

**Notebook Work:**
- `05_evaluation.ipynb`: Analyze results vs gold standard
- Identify failure patterns
- Calculate green metrics (tokens/persona, API calls, latency)

---

## Terminal Commands Reference (Learning Track)

### Essential Commands to Master

```bash
# Navigation & File Management
pwd                          # Print working directory
ls -lah                      # List all files with details
cd path/to/directory         # Change directory
mkdir -p src/utils           # Create nested directories
touch src/__init__.py        # Create empty file
cp -r src/ backup/           # Copy directory recursively
rm -rf cache/                # Remove directory (careful!)

# Python Development
python -m pytest             # Run tests
python -m pytest -k "test_name" -v  # Run specific test
python -m pytest --cov=src   # Run with coverage
python -m pip install -e .   # Install package in editable mode
python -c "import sys; print(sys.path)"  # Check Python path

# AWS CLI (SageMaker Context)
aws s3 cp s3://bucket/file.json ./data/  # Download from S3
aws s3 sync ./data/ s3://bucket/data/    # Sync directory to S3
aws s3 ls s3://bucket/ --recursive       # List all files

# Git (Version Control)
git status                   # Check status
git add src/                 # Stage changes
git commit -m "message"      # Commit
git log --oneline            # View history
git diff                     # See changes

# Process Management
ps aux | grep python         # Find Python processes
kill -9 <PID>                # Kill process
nohup python script.py &     # Run in background
jobs                         # List background jobs

# Monitoring & Debugging
tail -f logs/app.log         # Follow log file
grep -r "ERROR" logs/        # Search for errors
wc -l data/*.json            # Count lines in files
du -sh data/                 # Check directory size
```

### SageMaker-Specific Commands

```bash
# Check SageMaker role and permissions
aws sts get-caller-identity

# Monitor notebook instance
aws sagemaker describe-notebook-instance --notebook-instance-name your-instance

# Check available resources
df -h                        # Disk space
free -h                      # Memory usage
top                          # CPU and processes
```

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
```

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

Your existing `docs/ai_coding_instructions.md` should be referenced throughout development:

```bash
# Before starting a major feature
cat docs/ai_coding_instructions.md | grep -A 10 "Requirements"

# During implementation
# Reference sections as needed for best practices
```

The AI assistant should treat both this document and your `ai_coding_instructions.md` as authoritative guides for development decisions.

---

## Git Workflow & Best Practices (Solo Developer)

### Branching Strategy: Clean & Focused

-   **`main` branch**: This is your stable, production-ready branch. **Never commit directly to `main`**.
-   **Feature branches**: All work (new features, fixes, experiments) happens in a dedicated branch.
    -   **Naming**: `feature/node-name`, `fix/bug-description`, `refactor/utils-cleanup`
    -   **Create from `main`**: Always branch off the latest version of `main`.

```bash
# Get the latest stable code
git checkout main
git pull

# Create a new branch for your task
git checkout -b feature/persona-analysis-node
```

### Commit Hygiene: Atomic & Descriptive

-   **Commit small and often**: Each commit should represent a single, logical change.
-   **Write clear messages**: Follow a consistent format for clarity.
    -   Use imperative mood: `Add skill coverage utility` not `Added...`
    -   Keep the subject line concise (under 50 characters).
    -   Use the body to explain the "why," not the "how."

**Good Commit Example:**
```
feat: Add hard filter for location preferences

This commit introduces a non-negotiable filter to exclude jobs
that do not match the persona's location requirements.
```

### Solo Workflow Pattern

This simple, disciplined process keeps your project history clean and manageable.

1.  **Sync `main`**: `git checkout main && git pull`
2.  **Create a new branch**: `git checkout -b feature/my-new-feature`
3.  **Work & Commit**:
    -   Make your changes.
    -   Run tests (`pytest`).
    -   Commit your changes with a clear message: `git commit -m "feat: Implement X"`
4.  **Merge into `main`**:
    -   Switch back to main: `git checkout main`
    -   Merge your feature branch: `git merge --no-ff feature/my-new-feature` (The `--no-ff` flag preserves branch history).
5.  **Push your changes**: `git push origin main`
6.  **Clean up**:
    -   Delete the local branch: `git branch -d feature/my-new-feature`
    -   Delete the remote branch (if you pushed it): `git push origin --delete feature/my-new-feature`