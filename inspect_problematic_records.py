import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def inspect_problematic_records():
    """Inspect the exact structure of the failing records."""
    filepath = Path("output/submission_final.json")
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    # Check the specific records mentioned in the error
    problematic_indices = [8, 13, 16, 18]
    
    for idx in problematic_indices:
        record = data[idx]
        print(f"\n{'='*60}")
        print(f"Record {idx}: person_id={record['persona_id']}")
        print(f"{'='*60}")
        
        if 'jobs' in record:
            for job_idx, job in enumerate(record['jobs']):
                print(f"\n  Job {job_idx}:")
                print(f"    Type: {type(job)}")
                
                if isinstance(job, dict) and 'trainings' in job:
                    print(f"    Has 'trainings' key")
                    print(f"    Trainings type: {type(job['trainings'])}")
                    
                    if isinstance(job['trainings'], list):
                        for t_idx, training in enumerate(job['trainings'][:3]):  # First 3
                            print(f"      Training {t_idx}: type={type(training)}, value={training}")
                            
                elif isinstance(job, list):
                    print(f"    Job is a list with {len(job)} items")
                    for item_idx, item in enumerate(job[:2]):
                        print(f"      Item {item_idx}: type={type(item)}, value={item}")

if __name__ == "__main__":
    inspect_problematic_records()