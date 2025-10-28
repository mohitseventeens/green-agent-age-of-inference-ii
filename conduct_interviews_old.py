# conduct_interviews.py
import logging
import time
import argparse
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

from src.nodes import ExtractProfileNode, PersonaProfile
from src.utils.call_llm import COST_TRACKER

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
    
    # Ensure profile is serializable
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
    """Saves the interview run metadata."""
    path = output_dir / "interview_metadata.json"
    with path.open('w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    logger.info(f"Interview run metadata saved to {path}")

def main():
    """
    Conducts interviews for a range of personas, saving clean profiles
    and detailed conversation traces.
    """
    # ... (argparse logic remains the same) ...
    parser = argparse.ArgumentParser(description="Conduct interviews with personas and save their profiles.")
    parser.add_argument('--personas', type=str, default="1-3", help='A range of persona IDs, e.g., "1-10" or "5".')
    parser.add_argument(
        '--model', 
        type=str, 
        default="mistral-medium-latest",
        choices=["mistral-small-latest", "mistral-medium-latest", "mistral-large-latest"],
        help='The Mistral model to use for conducting the interviews.'
    )
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
    interviews_dir = Path("data") / "interviews" # New directory for traces
    profiles_dir.mkdir(parents=True, exist_ok=True)
    interviews_dir.mkdir(parents=True, exist_ok=True)
    
    extract_profile_node = ExtractProfileNode()
    extract_profile_node.set_params({"interview_model": args.model})
    
    run_start_time = time.time()
    successful_interviews = 0

    logger.info(f"--- 🎙️ Starting interviews for {len(persona_ids)} personas using model: {args.model} ---")

    for persona_id in tqdm(persona_ids, desc="Interviewing Personas"):
        try:
            shared = {"persona_id": persona_id}
            extract_profile_node.run(shared)
            
            # Save the detailed trace regardless of outcome
            save_interview_trace(persona_id, shared, interviews_dir)
            
            if "persona_profile" in shared:
                save_profile(persona_id, shared["persona_profile"], profiles_dir)
                successful_interviews += 1
            else:
                logger.error(f"Interview with {persona_id} finished, but no profile was extracted.")

        except Exception as e:
            logger.error(f"FATAL error during interview with {persona_id}: {e}", exc_info=True)

    run_end_time = time.time()

    # --- Collect and Save Metadata ---
    metadata = {
        "run_timestamp_utc": datetime.utcnow().isoformat(),
        "interview_model_used": args.model,
        "persona_range_processed": args.personas,
        "total_personas_requested": len(persona_ids),
        "successful_interviews": successful_interviews,
        "total_execution_seconds": round(run_end_time - run_start_time, 2),
        "avg_seconds_per_persona": round((run_end_time - run_start_time) / len(persona_ids), 2) if persona_ids else 0,
        "cost_and_tokens": COST_TRACKER
    }
    # Save metadata inside the interviews directory as it pertains to that run
    save_interview_metadata(metadata, interviews_dir) 

    logger.info("\n--- ✅ Interview Session Complete ---")
    logger.info(f"Successfully interviewed {successful_interviews}/{len(persona_ids)} personas.")
    logger.info(f"Clean profiles saved in '{profiles_dir}'.")
    logger.info(f"Detailed interview traces saved in '{interviews_dir}'.")
    logger.info(f"Execution Time: {metadata['total_execution_seconds']}s")
    logger.info(f"Total Cost: ${metadata['cost_and_tokens']['total_cost']:.4f}")

if __name__ == "__main__":
    main()