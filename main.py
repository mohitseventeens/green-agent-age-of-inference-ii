# MODIFIED: main.py

from dotenv import load_dotenv
load_dotenv()

import argparse
import json
import logging
import os
import time
from pathlib import Path
from tqdm import tqdm
from src.flow import create_main_flow
# Import the global cost tracker
from src.utils.call_llm import COST_TRACKER

# (logging setup code remains the same)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# (run_for_persona and save_trace_log functions remain the same)
def run_for_persona(flow, persona_id: str) -> dict:
    logger.info(f"--- Processing persona: {persona_id} ---")
    shared = {"persona_id": persona_id}
    if "parsed_jobs" not in shared_cache:
        logger.info("First run: Executing load and parse nodes...")
        initial_shared = {}
        flow.start_node._run(initial_shared)
        flow.start_node.successors["default"]._run(initial_shared)
        shared_cache["parsed_jobs"] = initial_shared.get("parsed_jobs", [])
        shared_cache["parsed_trainings"] = initial_shared.get("parsed_trainings", [])
        logger.info("Load and parse results are now cached.")
    shared["parsed_jobs"] = shared_cache["parsed_jobs"]
    shared["parsed_trainings"] = shared_cache["parsed_trainings"]
    persona_flow_start_node = flow.start_node.successors["default"].successors["default"]
    current_node = persona_flow_start_node
    last_action = None
    while current_node:
        last_action = current_node._run(shared)
        current_node = flow.get_next_node(current_node, last_action)
    return shared

def save_trace_log(persona_id: str, shared_state: dict, output_dir: Path, metrics: dict):
    log_path = output_dir / f"{persona_id}_trace.json"
    trace_data = {
        "persona_id": shared_state.get("persona_id"),
        "metrics": metrics,
        "conversation_history": shared_state.get("conversation_history"),
        "persona_profile": shared_state.get("persona_profile").model_dump() if shared_state.get("persona_profile") else None,
        "decision_action": shared_state.get("decision_action"),
        "intermediate_recommendations": shared_state.get("intermediate_recommendations"),
        "final_recommendation": shared_state.get("final_recommendation")
    }
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(trace_data, f, indent=2, ensure_ascii=False)
    logger.info(f"Saved detailed trace with metrics to {log_path}")

def main():
    # (argparse setup remains the same)
    parser = argparse.ArgumentParser(description="Run the Green Agent system.")
    parser.add_argument('--personas', type=str, default="1-3", help='A range of persona IDs, e.g., "1-10" or "5".')
    args = parser.parse_args()
    try:
        if "-" in args.personas:
            start_id, end_id = map(int, args.personas.split('-'))
        else:
            start_id = end_id = int(args.personas)
        persona_ids = [f"persona_{i:03d}" for i in range(start_id, end_id + 1)]
    except ValueError:
        logger.error(f"Invalid persona range: '{args.personas}'.")
        return

    # --- Setup ---
    output_dir = Path("output")
    logs_dir = output_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    main_flow = create_main_flow()
    all_recommendations = []
    total_start_time = time.time()

    logger.info(f"Starting run for {len(persona_ids)} personas: {persona_ids[0]} to {persona_ids[-1]}")

    # --- Main Execution Loop ---
    for persona_id in tqdm(persona_ids, desc="Processing Personas"):
        persona_start_time = time.time()
        try:
            final_shared_state = run_for_persona(main_flow, persona_id)
            persona_end_time = time.time()

            # --- Capture Metrics ---
            persona_metrics = {
                "execution_time_seconds": round(persona_end_time - persona_start_time, 2),
            }

            save_trace_log(persona_id, final_shared_state, logs_dir, persona_metrics)

            if "final_recommendation" in final_shared_state:
                all_recommendations.append(final_shared_state["final_recommendation"])
            else:
                logger.warning(f"No final recommendation for {persona_id}.")
                
        except Exception as e:
            logger.error(f"FATAL error processing {persona_id}: {e}", exc_info=True)
            all_recommendations.append({"persona_id": persona_id, "predicted_type": "awareness", "predicted_items": "error"})

    # --- Save Final Submission & Report Metrics ---
    total_end_time = time.time()
    submission_path = output_dir / "submission.json"
    with open(submission_path, 'w', encoding='utf-8') as f:
        json.dump(all_recommendations, f, indent=2, ensure_ascii=False)
    
    logger.info(f"\n--- ✅ FINAL SUMMARY ---")
    logger.info(f"Processing complete for {len(persona_ids)} personas.")
    logger.info(f"Total execution time: {total_end_time - total_start_time:.2f} seconds.")
    logger.info(f"Average time per persona: {(total_end_time - total_start_time) / len(persona_ids):.2f} seconds.")
    logger.info(f"Submission file saved to {submission_path}")
    logger.info(f"Detailed logs saved in '{logs_dir}'.")
    
    logger.info("\n--- 📊 Cost & Token Usage ---")
    logger.info(f"Estimated Total Cost: ${COST_TRACKER['total_cost']:.4f}")
    for model, data in COST_TRACKER['by_model'].items():
        logger.info(f"  - Model: {model}")
        logger.info(f"    - API Calls: {data['calls']}")
        logger.info(f"    - Total Tokens: {data['input_tokens'] + data['output_tokens']}")
        logger.info(f"    - Estimated Cost: ${data['cost']:.4f}")


if __name__ == "__main__":
    shared_cache = {}
    main()