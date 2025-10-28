# parse_data.py
import logging
import time
import argparse
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from src.nodes import LoadStaticDataNode, ParseStaticDataNode
from src.utils.call_llm import COST_TRACKER

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def save_metadata(metadata: dict):
    """Saves the parsing run metadata to a JSON file."""
    path = Path("data") / "parsing_metadata.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    logger.info(f"Parsing metadata saved to {path}")

def main():
    """
    Runs the data loading and parsing pipeline and saves the structured
    results to cache files for the main application to use.
    Accepts a --sample argument to process only a subset of the data for testing.
    """
    parser = argparse.ArgumentParser(description="Parse job and training markdown files into structured JSON.")
    parser.add_argument('--sample', type=int, help='Parse only the first N jobs and trainings. Processes all if not specified.')
    args = parser.parse_args()

    logger.info("--- 🚀 Starting Standalone Data Parsing Script ---")
    if args.sample:
        logger.warning(f"--- RUNNING IN SAMPLE MODE: Processing only the first {args.sample} items ---")
    
    run_start_time = time.time()
    
    # 1. Instantiate nodes
    load_node = LoadStaticDataNode()
    parse_node = ParseStaticDataNode()
    parse_node.set_params({"parsing_model": "mistral-large-latest"})
    
    shared = {}
    
    # 2. Load raw data
    logger.info("--- Step 1: Loading raw markdown files ---")
    load_node.run(shared)

    jobs_to_parse = shared["all_jobs"]
    trainings_to_parse = shared["all_trainings"]

    if args.sample:
        jobs_to_parse = jobs_to_parse[:args.sample]
        trainings_to_parse = trainings_to_parse[:args.sample]
    
    # 3. Parse jobs
    logger.info(f"--- Step 2a: Parsing {len(jobs_to_parse)} jobs ---")
    jobs_start_time = time.time()
    shared["all_jobs"] = jobs_to_parse
    shared["all_trainings"] = [] # Temporarily empty to only parse jobs
    parse_node.run(shared)
    jobs_end_time = time.time()
    parsed_jobs = shared.get("parsed_jobs", [])

    # 4. Parse trainings
    logger.info(f"--- Step 2b: Parsing {len(trainings_to_parse)} trainings ---")
    trainings_start_time = time.time()
    shared["all_jobs"] = [] # Temporarily empty
    shared["all_trainings"] = trainings_to_parse
    parse_node.run(shared)
    trainings_end_time = time.time()
    parsed_trainings = shared.get("parsed_trainings", [])

    run_end_time = time.time()

    # 5. Collect and save metadata
    job_duration = jobs_end_time - jobs_start_time
    training_duration = trainings_end_time - trainings_start_time
    total_parsed_jobs = len(parsed_jobs)
    total_parsed_trainings = len(parsed_trainings)
    
    metadata = {
        "run_timestamp_utc": datetime.utcnow().isoformat(),
        "is_sample_run": bool(args.sample),
        "sample_size": args.sample if args.sample else None,
        "total_execution_seconds": round(run_end_time - run_start_time, 2),
        "parsing_model_used": "mistral-large-latest",
        "jobs_metadata": {
            "count_parsed": total_parsed_jobs,
            "total_seconds": round(job_duration, 2),
            "avg_seconds_per_job": round(job_duration / total_parsed_jobs, 2) if total_parsed_jobs > 0 else 0
        },
        "trainings_metadata": {
            "count_parsed": total_parsed_trainings,
            "total_seconds": round(training_duration, 2),
            "avg_seconds_per_training": round(training_duration / total_parsed_trainings, 2) if total_parsed_trainings > 0 else 0
        },
        "cost_and_tokens": COST_TRACKER
    }
    save_metadata(metadata)

    # 6. Final Report
    logger.info("\n--- ✅ Parsing Complete ---")
    if args.sample:
        logger.warning(f"--- NOTE: Output files are from a sample run of {args.sample} items. ---")
    logger.info(f"Execution Time: {metadata['total_execution_seconds']}s")
    logger.info(f"Total Cost: ${metadata['cost_and_tokens']['total_cost']:.4f}")

if __name__ == "__main__":
    main()