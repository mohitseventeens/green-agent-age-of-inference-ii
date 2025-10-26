import logging
from pathlib import Path
from typing import List, Dict, Literal

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def load_all_data(data_type: Literal["jobs", "trainings"]) -> List[Dict[str, str]]:
    """
    Loads all markdown files from the specified data directory.

    This function looks for the 'data' directory starting from the
    parent of the current script's location, making it robust to
    being called from different working directories (e.g., /src, /tests, /).

    Args:
        data_type: The type of data to load, either "jobs" or "trainings".

    Returns:
        A list of dictionaries, where each dictionary contains the 'id'
        (from the filename) and 'content' of a markdown file.
        Returns an empty list if the directory is not found.
    """
    # --- Robust Path Resolution ---
    # Assumes the script is in a subdirectory of the project root (e.g., src/utils)
    # and navigates up to find the 'data' directory.
    base_path = Path(__file__).resolve().parent.parent.parent
    data_dir = base_path / 'data' / data_type

    if not data_dir.exists():
        logger.error(f"Data directory not found at: {data_dir}")
        return []

    loaded_data = []
    files = sorted(data_dir.glob('*.md'))
    
    for file_path in files:
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            item_id = file_path.stem  # .stem gets the filename without extension
            loaded_data.append({'id': item_id, 'content': content})
        except Exception as e:
            logger.warning(f"Could not read or process file {file_path}: {e}")
            
    logger.info(f"Successfully loaded {len(loaded_data)} items from '{data_dir}'")
    return loaded_data

if __name__ == '__main__':
    print("--- Running Self-Test for data_retrieval utility ---")
    
    jobs_data = load_all_data("jobs")
    if jobs_data:
        print(f"\nLoaded {len(jobs_data)} job postings.")
        print("Sample job item:")
        print(f"  ID: {jobs_data[0]['id']}")
        print(f"  Content snippet: {jobs_data[0]['content'][:100].strip()}...")
    else:
        print("\nCould not load job postings. Check directory path.")

    trainings_data = load_all_data("trainings")
    if trainings_data:
        print(f"\nLoaded {len(trainings_data)} training programs.")
        print("Sample training item:")
        print(f"  ID: {trainings_data[0]['id']}")
        print(f"  Content snippet: {trainings_data[0]['content'][:100].strip()}...")
    else:
        print("\nCould not load training programs. Check directory path.")
    
    print("\n--- Self-Test Complete ---")
