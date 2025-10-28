import logging
import time
import argparse
import json
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

from src.flow import create_recommendation_flow
from src.nodes import PersonaProfile, JobProfile, TrainingProfile
from src.utils.call_llm import COST_TRACKER

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- NEW: Function to save the detailed trace ---
def save_recommendation_trace(persona_id: str, shared_state: dict, output_dir: Path):
    """Saves a detailed trace of the recommendation generation process."""
    trace_path = output_dir / f"{persona_id}_recommendation_trace.json"
    
    # Clean up Pydantic models for JSON serialization
    profile_dump = shared_state.get("persona_profile").model_dump() if shared_state.get("persona_profile") else {}
    
    trace_details = shared_state.get("trace_details", {})
    if "job_ranking" in trace_details:
        trace_details["job_ranking"] = [
            {
                "job": item["job"].model_dump(),
                "score": item["score"],
                "sub_scores": item["sub_scores"]
            } for item in trace_details["job_ranking"]
        ]
    if "training_ranking" in trace_details:
        trace_details["training_ranking"] = [
            {
                "training": item["training"].model_dump(),
                "score": item["score"],
                "sub_scores": item["sub_scores"]
            } for item in trace_details["training_ranking"]
        ]

    trace_data = {
        "persona_id": persona_id,
        "persona_profile": profile_dump,
        "decision_action": shared_state.get("decision_action"),
        "trace_details": trace_details,
        "final_recommendation": shared_state.get("final_recommendation")
    }
    
    with trace_path.open('w', encoding='utf-8') as f:
        json.dump(trace_data, f, indent=2, ensure_ascii=False)
    logger.debug(f"Saved recommendation trace for {persona_id} to {trace_path}")

def run_for_persona(flow, persona_profile: PersonaProfile, parsed_data: dict) -> dict:
    """Runs the recommendation part of the flow for a single persona."""
    logger.info(f"--- Generating recommendation for: {persona_profile.persona_id} ---")
    
    shared = {
        "persona_id": persona_profile.persona_id,
        "persona_profile": persona_profile,
        "parsed_jobs": parsed_data["parsed_jobs"],
        "parsed_trainings": parsed_data["parsed_trainings"],
        "trace_details": {} # Initialize the trace dict
    }
    
    flow.run(shared)
    return shared

# def main():
#     # This is a simplified main function for debugging.
#     # It removes the try/except block and resumability to get a clear error.
    
#     parser = argparse.ArgumentParser(description="DEBUGGING recommendation generation.")
#     parser.add_argument('--personas', type=str, required=True, help='A single persona ID, e.g., "2".')
#     args = parser.parse_args()
    
#     persona_id_to_process = f"persona_{int(args.personas):03d}"
#     logger.info(f"--- 🐞 DEBUGGING for single persona: {persona_id_to_process} ---")

#     # --- Load Data (same as before) ---
#     with open("data/parsed_jobs.json", 'r') as f:
#         parsed_jobs_data = [JobProfile.model_validate(j) for j in json.load(f)]
#     with open("data/parsed_trainings.json", 'r') as f:
#         parsed_trainings_data = [TrainingProfile.model_validate(t) for t in json.load(f)]
#     parsed_data = {"parsed_jobs": parsed_jobs_data, "parsed_trainings": parsed_trainings_data}
    
#     profile_file = Path(f"data/profiles/{persona_id_to_process}.json")
#     with open(profile_file, 'r') as f:
#         profile_data = json.load(f)
#         profile_data['persona_id'] = profile_file.stem
#         persona_profile = PersonaProfile.model_validate(profile_data)

#     # --- Run Flow (NO TRY/EXCEPT) ---
#     rec_flow = create_recommendation_flow()
    
#     # This will now crash exactly where the error is.
#     final_shared = run_for_persona(rec_flow, persona_profile, parsed_data)
    
#     if "final_recommendation" in final_shared:
#         print("\n--- ✅ SUCCESS ---")
#         print("Final recommendation that would have been saved:")
#         print(json.dumps(final_shared["final_recommendation"], indent=2))
#     else:
#         print("\n--- ❌ FAILURE ---")
#         print("Flow ran but produced no final recommendation.")
# In generate_recommendations.py, replace the main() function with this:

# def main():
#     parser = argparse.ArgumentParser(description="Generate recommendations and detailed traces for persona profiles.")
#     parser.add_argument('--personas', type=str, help='Optional: A range of persona IDs, e.g., "1-10".')
#     args = parser.parse_args()

#     # --- Load Static Data ---
#     try:
#         with open("data/parsed_jobs.json", 'r') as f:
#             parsed_jobs_data = [JobProfile.model_validate(j) for j in json.load(f)]
#         with open("data/parsed_trainings.json", 'r') as f:
#             parsed_trainings_data = [TrainingProfile.model_validate(t) for t in json.load(f)]
#         parsed_data = {"parsed_jobs": parsed_jobs_data, "parsed_trainings": parsed_trainings_data}
#     except FileNotFoundError as e:
#         logger.error(f"Could not load parsed data. Run 'parse_data.py' first. Error: {e}")
#         return

#     # --- Load Persona Profiles ---
#     profiles_dir = Path("data/profiles")
#     all_profile_files = sorted(profiles_dir.glob("persona_*.json"))
    
#     profiles_to_process_files = []
#     if args.personas:
#         try:
#             start_id, end_id = map(int, args.personas.split('-'))
#             requested_ids = {f"persona_{i:03d}" for i in range(start_id, end_id + 1)}
#             profiles_to_process_files = [pf for pf in all_profile_files if pf.stem in requested_ids]
#         except ValueError:
#             logger.error(f"Invalid persona range format: '{args.personas}'. Use 'start-end', e.g., '1-10'.")
#             return
#     else:
#         profiles_to_process_files = all_profile_files

#     if not profiles_to_process_files:
#         logger.error("No persona profiles found to process.")
#         return

#     # --- Setup Directories and Flow ---
#     output_dir = Path("output")
#     traces_dir = output_dir / "traces"
#     traces_dir.mkdir(parents=True, exist_ok=True)
#     rec_flow = create_recommendation_flow()
    
#     # --- Resumability Logic ---
#     submission_path = output_dir / "submission.json"
#     if submission_path.exists():
#         try:
#             with open(submission_path, 'r') as f:
#                 existing_recs = json.load(f)
#             existing_ids = {rec['persona_id'] for rec in existing_recs}
#             logger.info(f"Found {len(existing_ids)} existing recommendations in submission.json.")
#         except (json.JSONDecodeError, FileNotFoundError):
#             existing_recs = []
#             existing_ids = set()
#     else:
#         existing_recs = []
#         existing_ids = set()

#     new_profiles_to_process = [
#         pf for pf in profiles_to_process_files if pf.stem not in existing_ids
#     ]

#     if not new_profiles_to_process:
#         logger.info("--- All personas in the specified range have already been processed. Nothing to do. ---")
#         return

#     logger.info(f"--- 🧠 Starting/Resuming recommendation generation for {len(new_profiles_to_process)} new personas ---")
    
#     run_start_time = time.time()
    
#     newly_generated_recs = []
#     for profile_file in tqdm(new_profiles_to_process, desc="Generating New Recommendations"):
#         try:
#             with open(profile_file, 'r') as f:
#                 profile_data = json.load(f)
#                 profile_data['persona_id'] = profile_file.stem
#                 persona_profile = PersonaProfile.model_validate(profile_data)
            
#             final_shared = run_for_persona(rec_flow, persona_profile, parsed_data)
            
#             if "final_recommendation" in final_shared:
#                 newly_generated_recs.append(final_shared["final_recommendation"])
#                 save_recommendation_trace(persona_profile.persona_id, final_shared, traces_dir)
#             else:
#                  logger.error(f"Flow finished for {profile_file.stem}, but no final_recommendation was produced.")

#         except Exception as e:
#             logger.error(f"Error generating recommendation for {profile_file.stem}: {e}", exc_info=True)
#             newly_generated_recs.append({"persona_id": profile_file.stem, "predicted_type": "awareness", "predicted_items": "error"})

#     run_end_time = time.time()
    
#     # --- Save Submission File and Report Metrics ---
#     final_submission_list = existing_recs + newly_generated_recs
#     with open(submission_path, 'w') as f:
#         json.dump(final_submission_list, f, indent=2, ensure_ascii=False)

#     # --- Save Metadata ---
#     metadata = {
#         "last_run_timestamp_utc": datetime.utcnow().isoformat(),
#         "total_personas_in_submission": len(final_submission_list),
#         "personas_processed_this_run": len(newly_generated_recs),
#         "execution_seconds_this_run": round(run_end_time - run_start_time, 2),
#         "cost_and_tokens_this_run": COST_TRACKER
#     }
#     save_recommendation_metadata(metadata, output_dir)

#     logger.info("\n--- ✅ Recommendation Generation Complete ---")
#     logger.info(f"Processed {metadata['personas_processed_this_run']} new personas in {metadata['execution_seconds_this_run']:.2f}s.")
#     logger.info(f"Submission file now contains {metadata['total_personas_in_submission']} recommendations and is saved to {submission_path}")
#     logger.info(f"Detailed trace files saved to {traces_dir}")
#     logger.info(f"Estimated Cost This Run: ${COST_TRACKER['total_cost']:.4f}")
# In generate_recommendations.py, replace the main() function with this:

def main():
    parser = argparse.ArgumentParser(description="Generate recommendations and detailed traces for persona profiles.")
    parser.add_argument('--personas', type=str, help='Optional: A range of persona IDs, e.g., "1-10".')
    args = parser.parse_args()

    # --- Load Static Data ---
    try:
        with open("data/parsed_jobs.json", 'r') as f:
            parsed_jobs_data = [JobProfile.model_validate(j) for j in json.load(f)]
        with open("data/parsed_trainings.json", 'r') as f:
            parsed_trainings_data = [TrainingProfile.model_validate(t) for t in json.load(f)]
        parsed_data = {"parsed_jobs": parsed_jobs_data, "parsed_trainings": parsed_trainings_data}
    except FileNotFoundError as e:
        logger.error(f"Could not load parsed data. Run 'parse_data.py' first. Error: {e}")
        return

    # --- Load Persona Profiles ---
    profiles_dir = Path("data/profiles")
    all_profile_files = sorted(profiles_dir.glob("persona_*.json"))
    
    profiles_to_process_files = []
    if args.personas:
        try:
            start_id, end_id = map(int, args.personas.split('-'))
            requested_ids = {f"persona_{i:03d}" for i in range(start_id, end_id + 1)}
            profiles_to_process_files = [pf for pf in all_profile_files if pf.stem in requested_ids]
        except ValueError:
            logger.error(f"Invalid persona range format: '{args.personas}'. Use 'start-end', e.g., '1-10'.")
            return
    else:
        profiles_to_process_files = all_profile_files

    if not profiles_to_process_files:
        logger.error("No persona profiles found to process.")
        return

    # --- Setup Directories and Flow ---
    output_dir = Path("output")
    traces_dir = output_dir / "traces"
    traces_dir.mkdir(parents=True, exist_ok=True)
    rec_flow = create_recommendation_flow()
    
    # --- Resumability Logic ---
    submission_path = output_dir / "submission.json"
    if submission_path.exists():
        try:
            with open(submission_path, 'r', encoding='utf-8') as f:
                existing_recs = json.load(f)
            existing_ids = {rec['persona_id'] for rec in existing_recs}
            logger.info(f"Found {len(existing_ids)} existing recommendations in {submission_path}.")
        except (json.JSONDecodeError, FileNotFoundError):
            logger.warning(f"Could not read or decode {submission_path}. Starting fresh.")
            existing_recs = []
            existing_ids = set()
    else:
        existing_recs = []
        existing_ids = set()

    new_profiles_to_process = [
        pf for pf in profiles_to_process_files if pf.stem not in existing_ids
    ]

    if not new_profiles_to_process:
        logger.info("--- All personas in the specified range have already been processed. Nothing to do. ---")
        return

    logger.info(f"--- 🧠 Starting/Resuming recommendation generation for {len(new_profiles_to_process)} new personas ---")
    
    run_start_time = time.time()
    
    newly_generated_recs = []
    for profile_file in tqdm(new_profiles_to_process, desc="Generating New Recommendations"):
        try:
            # ... (the persona processing loop is unchanged)
            with open(profile_file, 'r') as f:
                profile_data = json.load(f)
                profile_data['persona_id'] = profile_file.stem
                persona_profile = PersonaProfile.model_validate(profile_data)
            
            final_shared = run_for_persona(rec_flow, persona_profile, parsed_data)
            
            if "final_recommendation" in final_shared:
                newly_generated_recs.append(final_shared["final_recommendation"])
                save_recommendation_trace(persona_profile.persona_id, final_shared, traces_dir)
            else:
                 logger.error(f"Flow finished for {profile_file.stem}, but no final_recommendation was produced.")

        except Exception as e:
            logger.error(f"Error generating recommendation for {profile_file.stem}: {e}", exc_info=True)
            newly_generated_recs.append({"persona_id": profile_file.stem, "predicted_type": "awareness", "predicted_items": "error"})

    run_end_time = time.time()
    
    # --- CORRECTED: Atomic Write for Submission File ---
    final_submission_list = existing_recs + newly_generated_recs
    temp_submission_path = submission_path.with_suffix(".json.tmp")
    with open(temp_submission_path, 'w', encoding='utf-8') as f:
        json.dump(final_submission_list, f, indent=2, ensure_ascii=False)
    temp_submission_path.rename(submission_path) # Atomic operation

    # --- CORRECTED: Atomic Write and Accumulation for Metadata ---
    metadata_path = output_dir / "recommendation_metadata.json"
    if metadata_path.exists():
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                final_metadata = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            final_metadata = {} # Start fresh if corrupted
    else:
        final_metadata = {}

    final_metadata["last_run_timestamp_utc"] = datetime.utcnow().isoformat()
    final_metadata["total_personas_in_submission"] = len(final_submission_list)
    # You can add more accumulating logic here if needed, e.g., total_cost
    
    temp_metadata_path = metadata_path.with_suffix(".json.tmp")
    with open(temp_metadata_path, 'w', encoding='utf-8') as f:
        json.dump(final_metadata, f, indent=2, ensure_ascii=False)
    temp_metadata_path.rename(metadata_path)

    logger.info("\n--- ✅ Recommendation Generation Complete ---")
    logger.info(f"Processed {len(newly_generated_recs)} new personas in {run_end_time - run_start_time:.2f}s.")
    logger.info(f"Submission file now contains {len(final_submission_list)} recommendations and is saved to {submission_path}")
    
if __name__ == "__main__":
    main()