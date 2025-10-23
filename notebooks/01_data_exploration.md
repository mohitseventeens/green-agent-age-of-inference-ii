## Understanding the Challenge Data

### The Mission (kinda cool actually)
We're helping young people in Brazil find green jobs. UNICEF partnership, climate action, meaningful careers - the whole deal. 
And because it's 2025 we will build AI agents that can sift through job descriptions and training programs, match them to people's profiles, and do it efficiently and ethically!

**The Brazilian green jobs landscape we're working with:**
- **Major cities**: São Paulo (finance & tech hub), Rio de Janeiro (energy & environment), Brasília (policy & government), Salvador (renewable energy), Recife (innovation centers)
- **Key sectors**: Renewable energy (solar, wind, hydro), sustainable agriculture, environmental consulting, green construction, waste management
- **Companies leading the charge**: Petrobras (transitioning to renewables), Vale (sustainable mining), Suzano (sustainable forestry), plus hundreds of green startups

We have a `data` directory with:
- **`jobs/`** - 200 job postings
- **`trainings/`** - 497 training programs

### Quick math reality check
697 items × however many personas we need to match = potentially expensive if we're not careful with API calls.

This is where being smart about it pays off. Literally.

```python
# Let's see what we're working with
from pathlib import Path

# Count files and get basic statistics
jobs_dir = Path('../data/jobs')
trainings_dir = Path('../data/trainings')

job_files = list(jobs_dir.glob('*.md')) if jobs_dir.exists() else []
training_files = list(trainings_dir.glob('*.md')) if trainings_dir.exists() else []

print(f"Dataset Overview:")
print(f"Jobs: {len(job_files)}")
print(f"Trainings: {len(training_files)}")
print(f"Total items: {len(job_files) + len(training_files)}")
```

```sh
Dataset Overview:
Jobs: 200
Trainings: 497
Total items: 697
```

### Let's look at a job posting
```markdown
# Helper function to peek at files
from IPython.display import Markdown, display

def display_markdown_file(path: str) -> None:
    """Display a markdown file in Jupyter - nothing fancy"""
    p = Path(path)
    if not p.exists():
        print(f"File not found: {p}")
        return
    content = p.read_text(encoding='utf-8', errors='ignore')
    display(Markdown(content))
```

```python
# Display a sample job
display_markdown_file(job_files[0])
```

```sh
# Join Us as a Financial Reporting Analyst!

**Are you ready to make an impact?** We're looking for a **Financial Reporting Analyst** in **Recife** to help strengthen our accounting and management operations through accurate financial analysis and reporting.

**What You'll Do:**
- Prepare and analyze financial reports to support business decision-making
- Conduct risk assessments to identify potential financial vulnerabilities
- Interpret financial data and present findings to stakeholders
- Support auditing processes and ensure compliance with reporting standards

**Who You Are:**
You're a **detail-oriented professional** with strong analytical skills and a solid foundation in financial reporting. You have:
- Technical education (Técnico level) in accounting, finance, or related field
- At least 1 year of experience in financial analysis or reporting
- Intermediate skills in risk assessment and financial reporting preparation
- Basic knowledge of auditing principles and data interpretation
- Fluency in Portuguese (Brazilian)

**Bonus Points if You Have:**
- Experience with financial software or reporting tools
- Additional certifications in accounting or financial analysis

**Ready to apply?** This position is based in Recife and requires Portuguese fluency. Show us your analytical skills and passion for financial reporting!
```

### And a training program

```python
# Display a sample training
display_markdown_file(training_files[0])
```

```sh
**Why take this course?**

The **Basic Financial Cost Analysis Training** will help you:

✅ Master expense evaluation and financial assessment techniques at a foundational level
✅ Apply best practices for transparency and compliance
✅ Strengthen your resume with a recognized credential

**Course Details:**
- **Duration:** 6 weeks
- **Format:** online
- **Language:** Portuguese (Brazil)
- **Certification:** Yes

**Prerequisites:**
None

This comprehensive program covers essential methods for analyzing business expenses and financial data. You'll learn to identify cost patterns, evaluate spending efficiency, and create meaningful financial reports that support decision-making.

Perfect for professionals entering finance roles or those looking to add analytical skills to their toolkit. The structured approach takes you from basic concepts to practical application, ensuring you can confidently handle real-world cost evaluation scenarios.

The hybrid learning format combines flexibility with structured guidance, making it ideal for working professionals. Upon completion, you'll receive a certification that validates your newly acquired analytical capabilities.

**Don't miss the chance to stand out—register today!**
```

### What you'll notice

Both jobs and trainings have:
- **Overview/Description** 
- **Location** (this matters for matching)
- **Prerequisites** (skills, experience levels)
- **Outcomes** (for trainings)

But here's the kicker: they're not consistently formatted. Some use different headers, different structures, different language. 
Our solution needs to handle this chaos gracefully. 

This is why we can't just use regex or simple parsing - we need something smarter: GenAI!

### Understanding Tokens - Your Cost Unit

LLMs are usually priced via tokens. Usually X$ "per 1 million tokens"

**Why tokens matter for our challenge:**
- **Cost control**: 697 job postings × 100 tokens each = 69,700 tokens to process
- **Speed**: More tokens = slower responses (matters when processing hundreds of items)  
- **Planning**: Models have token limits (128k for all Mistral models)

**Quick cost reality check:**
- Small model: 69,700 tokens ≈ $0.007 to classify all jobs
- Large model: Same task ≈ $0.14 (20x more expensive)
- For 697 items, choosing the right model matters!

**Pro tip**: Always start with the smallest model that can handle your task. You can always upgrade to larger models for complex reasoning later.|

### Model Comparison - The Money Talk

| Model Name           | Size / Version     | Input Cost (per 1M tokens)  | Output Cost (per 1M tokens)  | Context Window |
|----------------------|--------------------|-----------------------------|--------------------------|----------------|
| Mistral Large 24-11  | Large              | \$2.00                       | \$6.00                        | 128k tokens      |
| Mistral Medium 3     | Medium             | \$0.40                       | \$2.00                        | 128k tokens      |
| Mistral Small 3.1    | Small              | \$0.10                       | \$0.30                        | 128k tokens      |

**Real talk**: For most filtering/classification tasks, the small model is plenty good and 15x cheaper. Only use the big guns when you really need them.
We'll see an example in a minute. But first we need to talk about prompting.

### When to use large vs small models?

Looking at both responses, they seem pretty similar, right? Both extracted the key information correctly. So why would you ever pay 15x more for the large model?

**Small model wins when:**
- Simple extraction tasks (skills, location, yes/no questions)
- Consistent input format
- High-volume processing (like our 697 jobs)
- Budget constraints

**Large model wins when:**
- Complex reasoning required ("Would this person from Recife be successful in this São Paulo role given the cultural differences?")
- Ambiguous or poorly formatted input
- Nuanced analysis (understanding implicit requirements)
- Multi-step logical chains

## Using LLMs for Data Filtering

### The problem
We have 697 items in our dataset. How can we categorize them efficiently without manually reading everything?

### Why traditional approaches fail
**Regex and keyword matching** would be a nightmare here. Consider these challenges:
- Job titles vary: "Engenheiro de Energia Solar" vs "Solar Energy Engineer" vs "Renewable Systems Specialist"  
- Skills are described differently: "2 years experience" vs "minimum 24 months" vs "experiência de 2 anos"
- Location formats differ: "São Paulo, SP" vs "Greater São Paulo Area" vs "Estado de São Paulo"
- Requirements buried in paragraphs vs structured lists

**Rule-based classification** would need hundreds of if-then statements and constant maintenance.

### The LLM solution
LLMs understand **semantic meaning**, not just keywords:
- They recognize "energia renovável" and "renewable energy" as the same concept
- They infer experience levels from contextual clues
- They handle inconsistent formatting gracefully  
- They can extract implicit information (e.g., senior-level roles often mention "leadership")

### The trade-offs
- **Accuracy**: Much higher than regex, handles edge cases
- **Cost**: API calls add up - need to optimize model choice
- **Speed**: Slower than regex, but parallel processing helps
- **Consistency**: Good with proper prompt design

### This design works:

- ✅ Constrained outputs: Only 3 possible answers reduces hallucination
- ✅ Clear definitions: Explicit criteria for each level
- ✅ Simple instruction: 'Just respond with one word' forces compliance
- ✅ Context window: 'Analyze whole file' ensures complete understanding
- ✅ Large model default: Classification needs reasoning, not just pattern matching

### Pro tips for production:

- Start with large model for accuracy baseline
- Test small model on sample - might be sufficient
- Use temperature=0 for consistent classifications
- Consider few-shot examples for edge cases
- Always validate on known examples before scaling

### Batch Processing Strategy

When you're processing hundreds of items, you need to think about **scale optimization**:

**Why batch processing matters:**
- **API rate limits**: Most APIs limit requests per minute/hour
- **Progress tracking**: Users want to see something happening  
- **Error handling**: Individual failures shouldn't kill the whole job
- **Memory management**: Don't load all 697 files into memory at once
- **Cost monitoring**: Track spending as you go, not at the end

**Batch size considerations:**
- **Too small** (1-2 items): Lots of overhead, slow overall progress
- **Too large** (100+ items): Memory issues, harder to recover from errors
- **Sweet spot** (10-25 items): Balance between efficiency and manageability

**For our GDSC dataset:**
- 697 total items to process
- Average ~500 characters per item 
- At 10 items per batch = 70 batches total
- Estimated time: 70 batches × 2 seconds = ~2.5 minutes

---

## Exercises

### Exercise 1: Data analysis
Build some actual statistics about our dataset:

Your mission: analyze the dataset properly
What we want to know about Brazilian green jobs:
- Geographic distribution (São Paulo, Rio, Brasília, Salvador, Recife, etc.)
- Average token counts per category
- Most common skills mentioned
- Portuguese vs English content ratio
- Green job concentration by region

Hint: Use the classify function pattern we just built
Consider analyzing:
- Job titles: "Engenheiro Ambiental" vs "Environmental Engineer"
- Location patterns: "São Paulo, SP" vs "Greater São Paulo" vs "Interior de São Paulo"
- Brazilian-specific skills: Portuguese fluency, local regulations, regional travel

```python
# Setup
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import json
from collections import Counter, defaultdict
import re
import os
from tqdm import tqdm
from dotenv import load_dotenv

_ = load_dotenv()

# Make sure we can import the call_llm function
# This assumes the notebook is in the 'notebooks' directory
# and the function is in 'src/utils/call_llm.py'
sys.path.append('..') 
from src.utils.call_llm import call_llm

# Let's assume MISTRAL_API_KEY is set in the environment
# from dotenv import load_dotenv
# load_dotenv()

if not os.getenv("MISTRAL_API_KEY"):
    print("WARNING: MISTRAL_API_KEY not set. LLM calls will fail.")
    print("Please create a .env file in the project root or set the environment variable.")

# --- Data Loading ---
jobs_dir = Path('../data/jobs')
trainings_dir = Path('../data/trainings')
job_files = list(jobs_dir.glob('*.md')) if jobs_dir.exists() else []
training_files = list(trainings_dir.glob('*.md')) if trainings_dir.exists() else []
all_files = job_files + training_files

# --- LLM-based Extractor Function ---
def analyze_document(content: str) -> Dict:
    """Uses an LLM to extract structured data from a job/training document."""
    prompt = f"""
    Analyze the following job or training description from Brazil. Extract the specified information in a JSON format.

    - "city": The primary city. Choose from ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Recife', 'Other', 'Unspecified'].
    - "domain": A short, 2-3 word category (e.g., 'Financial Analysis', 'Solar Energy', 'Environmental Law').
    - "language": The main language. Choose from ['Portuguese', 'English', 'Mixed'].
    - "requires_portuguese": A boolean (true/false) if Portuguese fluency is explicitly required.
    - "brazilian_specifics": A list of any Brazilian-specific regulations or terms mentioned (e.g., 'CONAMA', 'CLT', 'Mata Atlântica').

    Document:
    ---
    {content}
    ---

    Respond ONLY with the JSON object.
    """
    try:
        response = call_llm(prompt=prompt, model="mistral-small-latest")
        # Clean up response in case of markdown formatting
        cleaned_response = re.sub(r'```json\n|\n```', '', response).strip()
        return json.loads(cleaned_response)
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error processing document: {e}")
        return {
            "city": "Error", "domain": "Error", "language": "Error",
            "requires_portuguese": False, "brazilian_specifics": []
        }

# --- Main Analysis Logic ---
print("📝 Exercise 1: Data analysis")
print("Use LLMs to extract domains from job titles and training content")
print("Count location mentions across major Brazilian cities")  
print("Calculate processing costs for different classification approaches")
print("Bonus: Identify uniquely Brazilian requirements (e.g., Portuguese fluency, CONAMA compliance)")
print("\n--- Starting Analysis (this may take a few minutes) ---")

analysis_results = []
# Using a subset for a quick demonstration. Change to `all_files` to run on the full dataset.
files_to_process = all_files[:20] # For quick testing
# files_to_process = all_files # For full analysis

for file_path in tqdm(files_to_process, desc="Analyzing Documents"):
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    if content:
        analysis_results.append(analyze_document(content))

# --- Aggregation and Reporting ---
city_counts = Counter(res['city'] for res in analysis_results if 'city' in res)
domain_counts = Counter(res['domain'] for res in analysis_results if 'domain' in res)
language_counts = Counter(res['language'] for res in analysis_results if 'language' in res)
portuguese_req_count = sum(1 for res in analysis_results if res.get('requires_portuguese', False))
brazilian_specifics = [spec for res in analysis_results if 'brazilian_specifics' in res for spec in res['brazilian_specifics']]
specifics_counts = Counter(spec for spec in brazilian_specifics if spec) # Filter out empty strings

total_chars = sum(len(p.read_text(encoding='utf-8', errors='ignore')) for p in files_to_process)
# Approximation: 1 token ~ 4 characters
total_tokens_approx = total_chars / 4

print("\n--- 📊 Dataset Analysis Results ---")
print(f"\n📍 Geographic Distribution (Top 5):")
for city, count in city_counts.most_common(5):
    print(f"- {city}: {count} listings")

print(f"\n📚 Top 5 Job/Training Domains:")
for domain, count in domain_counts.most_common(5):
    print(f"- {domain}: {count} listings")

print(f"\n🗣️ Language Distribution:")
for lang, count in language_counts.items():
    print(f"- {lang}: {count} listings")

print(f"\n🇧🇷 Brazilian-Specific Insights:")
print(f"- Listings explicitly requiring Portuguese: {portuguese_req_count} ({portuguese_req_count/len(analysis_results):.1%})")
if specifics_counts:
    print(f"- Most common specific terms: {specifics_counts.most_common(3)}")
else:
    print("- No specific Brazilian terms were commonly found.")

print(f"\n- Estimated total tokens in dataset: {total_tokens_approx:,.0f}")
```

```sh
📝 Exercise 1: Data analysis
Use LLMs to extract domains from job titles and training content
Count location mentions across major Brazilian cities
Calculate processing costs for different classification approaches
Bonus: Identify uniquely Brazilian requirements (e.g., Portuguese fluency, CONAMA compliance)

--- Starting Analysis (this may take a few minutes) ---
Analyzing Documents: 100%|██████████| 20/20 [00:20<00:00,  1.05s/it]

--- 📊 Dataset Analysis Results ---

📍 Geographic Distribution (Top 5):
- Unspecified: 8 listings
- Recife: 3 listings
- Rio de Janeiro: 3 listings
- Other: 2 listings
- Brasília: 2 listings

📚 Top 5 Job/Training Domains:
- Insurance Compliance: 2 listings
- Food Production: 1 listings
- Visual Production: 1 listings
- Food Safety: 1 listings
- Procurement Analysis: 1 listings

🗣️ Language Distribution:
- Portuguese: 13 listings
- Mixed: 7 listings

🇧🇷 Brazilian-Specific Insights:
- Listings explicitly requiring Portuguese: 20 (100.0%)
- Most common specific terms: [('CLT', 3), ('HACCP', 1), ('GMP', 1)]

- Estimated total tokens in dataset: 7,565
```

### Exercise 2: Cost optimization
Figure out the cheapest way to process everything:

Cost comparison challenge
Calculate costs for:
1. All 697 items with small model
2. All 697 items with large model
3. Hybrid: small for classification, large for complex analysis

```python
# Cost comparison challenge
# Calculate costs for:
# 1. All 697 items with small model
# 2. All 697 items with large model
# 3. Hybrid: small for classification, large for complex analysis

print("📝 Exercise 2: Cost optimization")
print("Which approach gives best quality/cost ratio?")
print("What's the break-even point?")

# --- Cost Data (from notebook) ---
# Prices per 1 Million tokens (Input)
COSTS = {
    "small": 0.10,
    "large": 2.00
}

# Total tokens from previous exercise
# If exercise 1 was not run, we can re-calculate it here
if 'total_tokens_approx' not in locals():
    all_files = list(Path('../data/jobs').glob('*.md')) + list(Path('../data/trainings').glob('*.md'))
    total_chars = sum(len(p.read_text(encoding='utf-8', errors='ignore')) for p in all_files)
    total_tokens_approx = total_chars / 4

print(f"\n--- Cost Calculation based on ~{total_tokens_approx:,.0f} input tokens ---")

# --- Scenario 1: All Small ---
cost_all_small = (total_tokens_approx / 1_000_000) * COSTS["small"]
print(f"1. All Small Model: ${cost_all_small:.4f}")

# --- Scenario 2: All Large ---
cost_all_large = (total_tokens_approx / 1_000_000) * COSTS["large"]
print(f"2. All Large Model: ${cost_all_large:.4f}")

# --- Scenario 3: Hybrid Approach ---
# Assumption: 90% of tasks (like initial filtering/classification) use the small model.
# The remaining 10% of complex items require the large model for deeper analysis.
hybrid_ratio_small = 0.90
hybrid_ratio_large = 0.10
cost_hybrid = ((total_tokens_approx * hybrid_ratio_small / 1_000_000) * COSTS["small"]) + \
              ((total_tokens_approx * hybrid_ratio_large / 1_000_000) * COSTS["large"])
print(f"3. Hybrid Model (90% small, 10% large): ${cost_hybrid:.4f}")

print("\n--- Analysis ---")
print("✅ Best Quality/Cost Ratio: The Hybrid approach is almost always superior.")
print("   - It uses the cheap, fast small model for the majority of simple filtering and extraction tasks.")
print("   - It saves the expensive, powerful large model for the few items that require complex reasoning, nuance, or summarization.")
print("\n❓ Break-even Point: The 'break-even' isn't just about cost, but value.")
print("   - You should switch from small to large when the cost of an incorrect classification by the small model is greater than the extra cost of using the large model.")
print(f"   - For this dataset, the large model is {COSTS['large']/COSTS['small']:.0f}x more expensive. You only use it when its superior reasoning is absolutely necessary to get a correct result that the small model would fail on.")
```

```sh
📝 Exercise 2: Cost optimization
Which approach gives best quality/cost ratio?
What's the break-even point?

--- Cost Calculation based on ~7,565 input tokens ---
1. All Small Model: $0.0008
2. All Large Model: $0.0151
3. Hybrid Model (90% small, 10% large): $0.0022

--- Analysis ---
✅ Best Quality/Cost Ratio: The Hybrid approach is almost always superior.
   - It uses the cheap, fast small model for the majority of simple filtering and extraction tasks.
   - It saves the expensive, powerful large model for the few items that require complex reasoning, nuance, or summarization.

❓ Break-even Point: The 'break-even' isn't just about cost, but value.
   - You should switch from small to large when the cost of an incorrect classification by the small model is greater than the extra cost of using the large model.
   - For this dataset, the large model is 20x more expensive. You only use it when its superior reasoning is absolutely necessary to get a correct result that the small model would fail on.
```

### Exercise 3: Green jobs detector
Build a classifier for sustainability-related jobs:

```pthon
# Green jobs classifier for Brazilian context
def is_green_job(content: str) -> bool:
    """Detect sustainability/climate-related jobs and trainings in Brazilian context"""
    # Your implementation here
    # Look for keywords like: 
    # - English: renewable energy, sustainability, climate, environment, solar, wind
    # - Portuguese: energia renovável, sustentabilidade, meio ambiente, solar, eólica
    # - Brazilian specifics: CONAMA, Amazônia, Mata Atlântica, etanol, biodiesel
    # - Companies: Petrobras renewables, Vale sustainability, Suzano forestry
    pass
```

Implement the function and test it...
Consider Brazilian green job examples:
- Solar panel installer in Northeast Brazil
- Environmental consultant for mining companies  
- Sustainable agriculture specialist in Cerrado region
- Carbon credit analyst for forestry companies
- Renewable energy engineer for hydroelectric plants

```python
# Green jobs classifier for Brazilian context
def is_green_job(content: str) -> bool:
    """Detect sustainability/climate-related jobs and trainings in Brazilian context"""
    prompt = f"""
    You are an expert classifier for the Brazilian green economy. A 'green' job or training is one directly involved with environmental sustainability, renewable energy (solar, wind, hydro, biofuels), waste management, conservation, climate action, or sustainable resource management.

    Analyze the following text. Consider Brazilian specifics like 'energia renovável', 'sustentabilidade', 'meio ambiente', 'CONAMA', 'Amazônia', 'etanol', and the sustainability efforts of companies like Petrobras or Suzano.

    Based on this, is the following a 'green' opportunity? Respond with only the single word 'yes' or 'no'.

    ---
    {content}
    ---
    """
    try:
        # Use a small model as this is a simple, high-volume classification task
        response = call_llm(prompt=prompt, model="mistral-small-latest")
        return response.strip().lower() == 'yes'
    except Exception as e:
        print(f"An error occurred during classification: {e}")
        return False

print("📝 Exercise 3: Green jobs detector")
print("Build a classifier that recognizes sustainability jobs in both Portuguese and English")
print("Test it on the dataset - how many green opportunities can you find?")

# --- Implementation and Testing ---
green_jobs_count = 0
total_files_processed = 0

# Using a subset for a quick demonstration. Change to `all_files` to run on the full dataset.
files_to_process = all_files[:20] # For quick testing
# files_to_process = all_files # For full analysis

for file_path in tqdm(files_to_process, desc="Classifying Green Jobs"):
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    if content:
        if is_green_job(content):
            green_jobs_count += 1
        total_files_processed += 1

print(f"\n--- Classification Results ---")
if total_files_processed > 0:
    percentage = (green_jobs_count / total_files_processed) * 100
    print(f"Found {green_jobs_count} green opportunities out of {total_files_processed} total items ({percentage:.1f}%).")
else:
    print("No files were processed.")

print("\n--- Bonus Questions ---")
print("\n• What makes a job 'green' in the Brazilian context?")
print("""
  - Energy Sector: Roles in solar (especially Northeast), wind, hydroelectric power, and biofuels (etanol from sugarcane).
  - Natural Resources: Sustainable forestry (like Suzano), responsible mining (Vale's sustainability initiatives), and agribusiness focused on low-carbon practices.
  - Conservation: Work related to Brazil's unique biomes like the Amazônia and Mata Atlântica.
  - Regulation & Policy: Roles requiring knowledge of Brazilian environmental laws like CONAMA regulations.
  - Urban Sustainability: Jobs in waste management, green construction, and public policy in major cities.
""")

print("• How do green job requirements differ between São Paulo (urban) and Amazon region?")
print("""
  - São Paulo: Tends to have more corporate, tech, and finance-focused green jobs. Examples: ESG Analyst, Carbon Credit Trader, Green Tech Startup Developer, Sustainable Finance Manager. These are typically office-based and require business or tech degrees.
  - Amazon Region: Jobs are often field-based and hands-on. Examples: Conservation Scientist, Sustainable Forestry Manager, Ecotourism Guide, Environmental Compliance Officer for infrastructure projects. These roles often require degrees in biology, forestry, or environmental science and a willingness to work in remote locations.
""")

print("• Which green sectors are growing fastest in Brazil?")
print("""
  - Renewable Energy: Solar energy is booming, particularly in the sunny Northeast. Wind power is also a major growth area.
  - Biofuels: As a world leader in ethanol, Brazil continues to innovate in second-generation biofuels.
  - Carbon Markets & ESG: With increasing global pressure, corporate roles in ESG (Environmental, Social, and Governance) and carbon credit management are rapidly expanding, especially in financial hubs like São Paulo.
""")
```

```sh
📝 Exercise 3: Green jobs detector
Build a classifier that recognizes sustainability jobs in both Portuguese and English
Test it on the dataset - how many green opportunities can you find?
Classifying Green Jobs: 100%|██████████| 20/20 [00:07<00:00,  2.52it/s]

--- Classification Results ---
Found 2 green opportunities out of 20 total items (10.0%).

--- Bonus Questions ---

• What makes a job 'green' in the Brazilian context?

  - Energy Sector: Roles in solar (especially Northeast), wind, hydroelectric power, and biofuels (etanol from sugarcane).
  - Natural Resources: Sustainable forestry (like Suzano), responsible mining (Vale's sustainability initiatives), and agribusiness focused on low-carbon practices.
  - Conservation: Work related to Brazil's unique biomes like the Amazônia and Mata Atlântica.
  - Regulation & Policy: Roles requiring knowledge of Brazilian environmental laws like CONAMA regulations.
  - Urban Sustainability: Jobs in waste management, green construction, and public policy in major cities.

• How do green job requirements differ between São Paulo (urban) and Amazon region?

  - São Paulo: Tends to have more corporate, tech, and finance-focused green jobs. Examples: ESG Analyst, Carbon Credit Trader, Green Tech Startup Developer, Sustainable Finance Manager. These are typically office-based and require business or tech degrees.
  - Amazon Region: Jobs are often field-based and hands-on. Examples: Conservation Scientist, Sustainable Forestry Manager, Ecotourism Guide, Environmental Compliance Officer for infrastructure projects. These roles often require degrees in biology, forestry, or environmental science and a willingness to work in remote locations.

• Which green sectors are growing fastest in Brazil?

  - Renewable Energy: Solar energy is booming, particularly in the sunny Northeast. Wind power is also a major growth area.
  - Biofuels: As a world leader in ethanol, Brazil continues to innovate in second-generation biofuels.
  - Carbon Markets & ESG: With increasing global pressure, corporate roles in ESG (Environmental, Social, and Governance) and carbon credit management are rapidly expanding, especially in financial hubs like São Paulo.
```

## What we learned

✅ **Data structure**: 697 items in messy formats  
✅ **API basics**: Tokens, models, costs  
✅ **Smart filtering**: LLMs > regex for unstructured data  
✅ **Cost optimization**: Start small, scale strategically  

### The real lessons
- Token counting matters when you're processing lots of data
- Small models are surprisingly good for classification tasks
- Always track costs as you go