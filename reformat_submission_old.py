import json
import logging
from pathlib import Path

# --- Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """
    Reads submission.json, corrects formats for BOTH 'trainings_only' and
    the nested 'suggested_trainings', and saves to a new file.
    """
    input_path = Path("output/submission.json")
    output_path = Path("output/submission_final.json")

    logger.info(f"--- 🚀 Starting ADVANCED reformatting process for {input_path} ---")

    # 1. Read the source file
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            original_data = json.load(f)
        logger.info(f"Successfully read {len(original_data)} records.")
    except FileNotFoundError:
        logger.error(f"❌ ERROR: Source file not found at {input_path}.")
        return
    except json.JSONDecodeError:
        logger.error(f"❌ ERROR: Could not decode JSON from {input_path}.")
        return

    # 2. Process and reformat the data
    reformatted_data = []
    t_only_count = 0
    jt_count = 0
    for record in original_data:
        # --- FIX #1: For 'trainings_only' records ---
        if record.get("predicted_type") == "trainings_only":
            original_trainings = record.get("trainings", [])
            reformatted_trainings = [
                item["training_id"] for item in original_trainings if isinstance(item, dict)
            ]
            record["trainings"] = reformatted_trainings
            t_only_count += 1
        
        # --- FIX #2: For 'jobs+trainings' records (the new fix) ---
        elif record.get("predicted_type") == "jobs+trainings":
            for job_item in record.get("jobs", []):
                for suggested_training in job_item.get("suggested_trainings", []):
                    original_nested_trainings = suggested_training.get("trainings", [])
                    reformatted_nested_trainings = [
                        item["training_id"] for item in original_nested_trainings if isinstance(item, dict)
                    ]
                    suggested_training["trainings"] = reformatted_nested_trainings
            jt_count += 1

        reformatted_data.append(record)

    logger.info(f"Reformatted {t_only_count} 'trainings_only' records.")
    logger.info(f"Reformatted nested trainings for {jt_count} 'jobs+trainings' records.")

    # 3. Save to the destination file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(reformatted_data, f, indent=2, ensure_ascii=False)
    
    logger.info(f"--- ✅ Success! Saved {len(reformatted_data)} correctly formatted records to {output_path} ---")

if __name__ == "__main__":
    main()