import json
import os

def reformat_submission_for_api(input_filepath="output/submission.json", output_filepath="output/submission_final.json"):
    """
    Reads a submission JSON file from the specified path, reformats it
    into the correct API structure, and writes the result to a new file.

    This corrected version ensures that for the 'awareness' type, the
    'predicted_items' field is a simple string, as required by the API.

    Args:
        input_filepath (str): The path to the input JSON file.
        output_filepath (str): The path to write the reformatted JSON file.
    """
    print(f"Starting reformatting process for '{input_filepath}'...")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_filepath)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    try:
        with open(input_filepath, 'r') as f:
            original_data = json.load(f)
        print(f"Successfully loaded {len(original_data)} records from '{input_filepath}'")
    except FileNotFoundError:
        print(f"ERROR: Input file not found at '{input_filepath}'. Please ensure the file exists.")
        return
    except json.JSONDecodeError:
        print(f"ERROR: Could not decode JSON from '{input_filepath}'. The file may be corrupt or not valid JSON.")
        return

    reformatted_data = []

    for i, record in enumerate(original_data):
        new_record = {
            'persona_id': record['persona_id'],
            'predicted_type': record['predicted_type']
        }

        pred_type = record.get('predicted_type')

        if pred_type == 'jobs+trainings':
            reformatted_jobs = []
            if 'jobs' in record and isinstance(record['jobs'], list):
                for job in record['jobs']:
                    training_ids = []
                    if 'suggested_trainings' in job and job['suggested_trainings']:
                        for skill_group in job['suggested_trainings']:
                            if 'trainings' in skill_group:
                                for training in skill_group['trainings']:
                                    training_ids.append(training['training_id'])
                    
                    reformatted_jobs.append({
                        'job_id': job['job_id'],
                        'suggested_trainings': training_ids
                    })
            new_record['jobs'] = reformatted_jobs

        elif pred_type == 'trainings_only':
            training_ids = []
            if 'trainings' in record and isinstance(record['trainings'], list):
                training_ids = [t['training_id'] for t in record.get('trainings', [])]
            new_record['trainings'] = training_ids

        elif pred_type == 'awareness':
            # --- THIS IS THE CORRECTED PART ---
            # The API expects a direct string, not a list containing a string.
            if 'predicted_items' in record:
                 new_record['predicted_items'] = record['predicted_items']
        
        else:
            print(f"Warning: Record {i} (persona: {record.get('persona_id')}) has an unrecognized predicted_type: '{pred_type}'")

        reformatted_data.append(new_record)

    try:
        with open(output_filepath, 'w') as f:
            # Using a compact format for the final submission file
            json.dump(reformatted_data, f, indent=4)
        print(f"✅ Successfully reformatted data and saved to '{output_filepath}'")
    except IOError as e:
        print(f"ERROR: Could not write to file '{output_filepath}'. Reason: {e}")

if __name__ == '__main__':
    reformat_submission_for_api()