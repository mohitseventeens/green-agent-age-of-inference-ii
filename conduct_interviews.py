# conduct_interviews.py
import logging
import time
import argparse
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

# Make sure all necessary components are imported
from src.nodes import ExtractProfileNode, PersonaProfile
from src.utils.call_llm import COST_TRACKER, MISTRAL_PRICING

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def save_profile(persona_id: str, profile: PersonaProfile, output_dir: Path):
    """Saves only the final, clean persona profile."""
    profile_path = output_dir / f"{persona_id}.json"
    profile_dict = profile.model_dump()
    if 'persona_id' in profile_dict:
        del profile_dict['persona_id']
    with profile_path.open('w', encoding='utf-8') as f:
        json.dump(profile_dict, f, indent=2, ensure_ascii=False)
    logger.debug(f"Saved clean profile for {persona_id} to {profile_path}")

def save_interview_trace(persona_id: str, shared_state: dict, output_dir: Path):
    """Saves the detailed interview trace, including the conversation."""
    trace_path = output_dir / f"{persona_id}_trace.json"
    profile_dump = None
    if shared_state.get("persona_profile"):
        profile_dump = shared_state["persona_profile"].model_dump()
    trace_data = {
        "persona_id": persona_id,
        "final_profile": profile_dump,
        "conversation_history": shared_state.get("conversation_history", [])
    }
    with trace_path.open('w', encoding='utf-8') as f:
        json.dump(trace_data, f, indent=2, ensure_ascii=False)
    logger.debug(f"Saved full interview trace for {persona_id} to {trace_path}")

def save_interview_metadata(metadata: dict, output_dir: Path):
    """Saves or updates the interview run metadata."""
    path = output_dir / "interview_metadata.json"
    
    # Initialize the base structure for a new file
    final_metadata = {
        "last_run_timestamp_utc": metadata['run_timestamp_utc'],
        "total_execution_seconds": 0.0,
        "cost_and_tokens": {"total_cost": 0.0, "by_model": {}}
    }
    
    if path.exists():
        logger.info("Updating existing metadata file.")
        with path.open('r', encoding='utf-8') as f:
            final_metadata = json.load(f)
            # Ensure old keys exist for backward compatibility
            if 'total_execution_seconds' not in final_metadata:
                final_metadata['total_execution_seconds'] = 0.0
            if 'cost_and_tokens' not in final_metadata:
                final_metadata['cost_and_tokens'] = {"total_cost": 0.0, "by_model": {}}

    # Update simple fields
    final_metadata['last_run_timestamp_utc'] = metadata['run_timestamp_utc']
    final_metadata['total_execution_seconds'] += metadata['execution_seconds_this_run']
    
    # # Accumulate cost and token data
    # for model, data in metadata['cost_and_tokens']['by_model'].items():
    #     if model not in final_metadata['cost_and_tokens']['by_model']:
    #         final_metadata['cost_and_tokens']['by_model'][model] = data
    #     else:
    #         for key in ['calls', 'input_tokens', 'output_tokens', 'cost']:
    #             final_metadata['cost_and_tokens']['by_model'][model][key] += data[key]
    
    # --- CORRECTED: Accumulate cost and token data ---
    current_run_costs = metadata['cost_and_tokens']
    
    # Iterate over the models from the CURRENT run
    for model, data in current_run_costs['by_model'].items():
        # If the model is new to the final metadata, initialize it
        if model not in final_metadata['cost_and_tokens']['by_model']:
            final_metadata['cost_and_tokens']['by_model'][model] = {
                'calls': 0, 'input_tokens': 0, 'output_tokens': 0, 'cost': 0.0
            }
        
        # Add the current run's numbers to the final totals
        final_metadata['cost_and_tokens']['by_model'][model]['calls'] += data['calls']
        final_metadata['cost_and_tokens']['by_model'][model]['input_tokens'] += data['input_tokens']
        final_metadata['cost_and_tokens']['by_model'][model]['output_tokens'] += data['output_tokens']
        final_metadata['cost_and_tokens']['by_model'][model]['cost'] += data['cost']

    # Recalculate the grand total cost from the accumulated model costs
    final_metadata['cost_and_tokens']['total_cost'] = sum(
        m['cost'] for m in final_metadata['cost_and_tokens']['by_model'].values()
    )
    
    final_metadata['cost_and_tokens']['total_cost'] = sum(m['cost'] for m in final_metadata['cost_and_tokens']['by_model'].values())
        
    with path.open('w', encoding='utf-8') as f:
        json.dump(final_metadata, f, indent=2, ensure_ascii=False)
    logger.info(f"Interview run metadata saved to {path}")

def main():
    parser = argparse.ArgumentParser(description="Conduct interviews with personas and save their profiles.")
    parser.add_argument('--personas', type=str, default="1-100", help='A range of persona IDs, e.g., "1-10" or "5".')
    parser.add_argument('--model', type=str, default="mistral-medium-latest", choices=list(MISTRAL_PRICING.keys()), help='The Mistral model to use for interviews.')
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

    # --- Setup Directories and Nodes ---
    profiles_dir = Path("data") / "profiles"
    interviews_dir = Path("data") / "interviews"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    interviews_dir.mkdir(parents=True, exist_ok=True)
    
    extract_profile_node = ExtractProfileNode()
    extract_profile_node.set_params({"interview_model": args.model})
    
    run_start_time = time.time()
    successful_interviews_this_run = 0

    logger.info(f"--- 🎙️ Starting/Resuming interviews for {len(persona_ids)} personas using model: {args.model} ---")

    personas_to_interview = []
    for persona_id in persona_ids:
        profile_path = profiles_dir / f"{persona_id}.json"
        if profile_path.exists():
            logger.info(f"Skipping {persona_id}: Profile already exists.")
        else:
            personas_to_interview.append(persona_id)

    if not personas_to_interview:
        logger.info("--- All personas in the specified range have already been interviewed. Nothing to do. ---")
        return

    logger.info(f"--- Found {len(personas_to_interview)} new personas to interview. ---")

    for persona_id in tqdm(personas_to_interview, desc="Interviewing New Personas"):
        try:
            shared = {"persona_id": persona_id}
            extract_profile_node.run(shared)
            
            save_interview_trace(persona_id, shared, interviews_dir)
            
            if "persona_profile" in shared and shared["persona_profile"]:
                save_profile(persona_id, shared["persona_profile"], profiles_dir)
                successful_interviews_this_run += 1
            else:
                logger.error(f"Interview with {persona_id} finished, but no valid profile was extracted.")

        except Exception as e:
            logger.error(f"FATAL error during interview with {persona_id}: {e}", exc_info=True)

    run_end_time = time.time()

    # --- Collect and Save/Update Metadata ---
    metadata_this_run = {
        "run_timestamp_utc": datetime.utcnow().isoformat(),
        "execution_seconds_this_run": round(run_end_time - run_start_time, 2),
        "cost_and_tokens": COST_TRACKER
    }
    save_interview_metadata(metadata_this_run, interviews_dir)

    logger.info("\n--- ✅ Interview Session Complete ---")
    logger.info(f"Successfully interviewed {successful_interviews_this_run} new personas in this run.")
    total_profiles = len(list(profiles_dir.glob("*.json")))
    logger.info(f"Total profiles now available: {total_profiles}/100.")

if __name__ == "__main__":
    main()