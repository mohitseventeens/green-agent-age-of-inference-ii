## Understanding the Scoring System (This is Critical!)

Before we build anything, let's understand how your submission is actually scored. This knowledge alone can boost your score by 10-20%.

### The Two-Part Scoring Formula

Your final score = **50% Type Accuracy + 50% Recommendation Accuracy**

**Part 1: Type Accuracy (50% of your score)**
- Did you correctly predict if the persona needs `jobs+trainings`, `trainings_only`, or `awareness`?
- This is binary - you either get it right (1.0) or wrong (0.0)
- **Hidden gotcha**: Minors (age < 16) should ALWAYS get `awareness` type with `predicted_items: "too_young"`

**Part 2: Recommendation Accuracy (50% of your score)**
How this is calculated depends on the type:

For `jobs+trainings`:
- 25% of total score: F1 score on job matches
- 25% of total score: F1 score on training suggestions per job
- Yes, training suggestions matter that much!

For `trainings_only`:
- 50% of total score: F1 score on training recommendations

For `awareness`:
- 50% of total score: Exact match on reason (e.g., "too_young")

### The Critical Insight

**If you get the type wrong, your recommendation score is ZERO!**

Example: You recommend perfect jobs for someone, but they actually needed `trainings_only`. Your score for that persona: 0%.

This is why understanding personas is crucial. Getting the type right is literally half your score.

### Quick Win Strategy

1. **Check ages first** - Anyone under 16 → `awareness` with `predicted_items: "too_young"`
2. **Default to `jobs+trainings`** - Most personas want jobs
3. **Always include training suggestions** - They're 25% of your score for job recommendations!
   
### Understanding the Submission Format

**What's JSONL?** It's just JSON objects, one per line. Perfect for streaming large datasets without loading everything into memory.

```jsonl
{"persona_id": "persona_001", "predicted_type": "jobs+trainings", "jobs": [...]}
{"persona_id": "persona_002", "predicted_type": "jobs+trainings", "jobs": [...]}
```

[Learn more about JSONL format](https://jsonlines.org/) or ask Copilot (Ctrl+I) to explain the difference between JSON and JSONL.

Our `save_json()` function handles the conversion automatically!

### Getting to know the GDSC API

You sent your results to an endpoint just now with make_submission() function from utils.py. To learn more about the GDSC API and its documentation and endpoints, check out the GDSC API Documentation.md

# Matching Rules

To add extra clarity before you jump to work we wanted to share the basic matching rules that are used to define best matches. These rules are the baseline for decisions why certain persona is fit for a job. Although we all know that sometimes applying for a job you have no experience with could positively surprise you, **these hard filters exist for good reason**.

Think of them as the "minimum viable candidate" criteria. Ignore them at your own risk - your accuracy will tank.

## Hard Filters

- **Domain matches the persona's target domain**.
- **Location**:
  - If the persona has a defined city → the job must be in the same city or remote.
  - If the persona is "open to relocate" → there is no location constraint.
- **Languages include at least one in common**.
- **Education level** of the persona is equal to or greater than the job's requirement.
- **Experience**: persona's years of experience are equal to or greater than the job's requirement.

**Brazilian education levels** (in ascending order):

Ensino Fundamental < Ensino Médio < Técnico < Tecnólogo < Graduação < Bacharelado < Licenciatura < Pós-graduação < Especialização < Mestrado < MBA < Doutorado

**If any of these filters fail, the job must not be recommended.**

### Skills

If a persona lacks required skills for a job:
- The job must still be recommended (as long as it passes the hard filters).
- Trainings must be suggested to cover all missing skills.

Training recommendations must follow a strict level-by-level progression:
- If the persona has no knowledge of a skill and the job requires Intermediário, suggest both Básico and Intermediário (if available in the catalog).
- If the persona has Básico and the job requires Avançado, suggest Intermediário and Avançado (if available).
- More generally: if the persona is at level $p$ and the job requires $r$, you must propose all trainings available from $p+1$ to $r$.
- Missing levels in the catalog are acceptable. If no training exists for a given skill, the training list for that skill can remain empty (this is not a non-conformity).
Skills should never be a blocker: if someone wants a job that requires a certain skill, this should not prevent those jobs from being suggested (although for a better user experience, it makes sense to prioritize them first).

### Trainings

Trainings are available at three levels:

Básico → Intermediário → Avançado

Rules for training recommendations:
- A persona can only benefit from trainings above their current level.
- If the persona already knows a skill at Básico, recommend Intermediário or Avançado, but not Básico.
- In standalone training mode (when no jobs are being recommended):
  - Recommend only the next level above the current one.
  - If the persona has no prior level, recommend only Básico.
  - Do not suggest multiple levels at once in this mode.
- Personas may seek trainings either as a standalone goal or as preparation for a job.
- If no relevant training exists, the list may remain empty.

### Awareness

Some personas are not yet ready for jobs or trainings. In these cases, your assistant should provide awareness content to help them explore and learn.
Two possible cases:
- **Too young:** If the persona is under 16, return awareness content with the reason "too_young".
- **Seeking information:** If the persona is simply exploring (e.g., asking “What does an engineer do?”), return awareness content with the reason "info".

## Why These Rules Matter

**Example failure**: Recommending a Doutorado-level research position to someone with Ensino Médio education.
- **Human logic**: "Maybe they'll accept it anyway!"
- **Reality**: Automatic rejection, wastes everyone's time
- **Your score**: Takes a hit because it's an obviously bad match

**Example success**: Finding a remote sustainability job for someone in a small city with environmental interests.
- **Filters pass**: Location (remote), domain (environmental), experience level matches
- **Result**: Realistic recommendation that could actually work