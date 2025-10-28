# generate_recommendations.py
import logging
import time
import argparse
import json
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

from src.flow import create_recommendation_flow # Renamed from create_main_flow
from src.nodes import PersonaProfile, JobProfile, TrainingProfile
from src.utils.call_llm import COST_TRACKER

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_for_persona(flow, persona_profile: PersonaProfile, parsed_data: dict) -> dict:
    """Runs the recommendation part of the flow for a single, pre-interviewed persona."""
    logger.info(f"--- Generating recommendation for: {persona_profile.persona_id} ---")
    
    shared = {
        "persona_id": persona_profile.persona_id,
        "persona_profile": persona_profile,
        "parsed_jobs": parsed_data["parsed_jobs"],
        "parsed_trainings": parsed_data["parsed_trainings"]
    }
    
    # The flow now starts with the DecisionNode
    flow.run(shared)
    return shared

def main():
    parser = argparse.ArgumentParser(description="Generate recommendations for pre-interviewed persona profiles.")
    parser.add_argument('--personas', type=str, help='Optional: A range of persona IDs to process, e.g., "1-10". Processes all found profiles if not specified.')
    args = parser.parse_args()

    # --- Load Static Data ---
    try:
        with open("data/parsed_jobs.json", 'r') as f:
            parsed_jobs_data = [JobProfile.model_validate(j) for j in json.load(f)]
        with open("data/parsed_trainings.json", 'r') as f:
            parsed_trainings_data = [TrainingProfile.model_validate(t) for t in json.load(f)]
        parsed_data = {"parsed_jobs": parsed_jobs_data, "parsed_trainings": parsed_trainings_data}
    except FileNotFoundError as e:
        logger.error(f"Could not load parsed data. Please run 'parse_data.py' first. Error: {e}")
        return

    # --- Load Persona Profiles ---
    profiles_dir = Path("data/profiles")
    if not profiles_dir.exists():
        logger.error(f"Profiles directory not found at '{profiles_dir}'. Please run 'conduct_interviews.py' first.")
        return
        
    all_profile_files = sorted(profiles_dir.glob("persona_*.json"))
    
    # Filter profiles based on --personas argument if provided
    profiles_to_process = []
    if args.personas:
        start_id, end_id = map(int, args.personas.split('-'))
        requested_ids = {f"persona_{i:03d}" for i in range(start_id, end_id + 1)}
        for pf in all_profile_files:
            if pf.stem in requested_ids:
                profiles_to_process.append(pf)
    else:
        profiles_to_process = all_profile_files

    if not profiles_to_process:
        logger.error("No persona profiles found to process for the given range.")
        return

    # --- Run Recommendation Flow ---
    rec_flow = create_recommendation_flow()
    all_recommendations = []
    run_start_time = time.time()

    logger.info(f"--- 🧠 Starting recommendation generation for {len(profiles_to_process)} personas ---")

    for profile_file in tqdm(profiles_to_process, desc="Generating Recommendations"):
        try:
            with open(profile_file, 'r') as f:
                # Add persona_id to the profile data before validation
                profile_data = json.load(f)
                profile_data['persona_id'] = profile_file.stem
                persona_profile = PersonaProfile.model_validate(profile_data)
            
            final_shared = run_for_persona(rec_flow, persona_profile, parsed_data)
            if "final_recommendation" in final_shared:
                all_recommendations.append(final_shared["final_recommendation"])
        except Exception as e:
            logger.error(f"Error generating recommendation for {profile_file.stem}: {e}", exc_info=True)
            all_recommendations.append({"persona_id": profile_file.stem, "predicted_type": "awareness", "predicted_items": "error"})

    run_end_time = time.time()
    
    # --- Save Submission File and Report Metrics ---
    submission_path = Path("output") / "submission.json"
    submission_path.parent.mkdir(exist_ok=True)
    with open(submission_path, 'w') as f:
        json.dump(all_recommendations, f, indent=2, ensure_ascii=False)

    logger.info("\n--- ✅ Recommendation Generation Complete ---")
    logger.info(f"Total execution time: {run_end_time - run_start_time:.2f} seconds.")
    logger.info(f"Average time per persona: {(run_end_time - run_start_time) / len(profiles_to_process):.2f} seconds.")
    logger.info(f"Submission file for {len(all_recommendations)} personas saved to {submission_path}")
    
    logger.info("\n--- 📊 Cost & Token Usage for Recommendations ---")
    logger.info(f"Estimated Total Cost: ${COST_TRACKER['total_cost']:.4f}")
    if COST_TRACKER['by_model']:
        for model, data in COST_TRACKER['by_model'].items():
            logger.info(f"  - Model: {model}, Cost: ${data['cost']:.4f}, Calls: {data['calls']}")

if __name__ == "__main__":
    main()