import argparse
import json
import logging
from pathlib import Path
from dotenv import load_dotenv

from src.utils.gdsc_utils import (
    validate_submission_format,
    make_submission,
    fetch_my_submissions,
    read_json,
)

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Main function to handle command-line arguments for submission tasks."""
    parser = argparse.ArgumentParser(
        description="A utility script to validate, submit, and manage GDSC competition submissions."
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # --- Validate Command ---
    parser_validate = subparsers.add_parser(
        "validate", help="Validate the format of a submission file without sending it."
    )
    parser_validate.add_argument(
        "filepath",
        nargs="?",
        default="output/submission.json",
        help="Path to the submission JSON file to validate (default: output/submission.json)",
    )

    # --- Submit Command ---
    parser_submit = subparsers.add_parser(
        "submit", help="Submit a recommendation file to the competition API."
    )
    parser_submit.add_argument(
        "filepath",
        nargs="?",
        default="output/submission.json",
        help="Path to the submission JSON file to submit (default: output/submission.json)",
    )
    parser_submit.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate the file and simulate submission without actually sending to the API.",
    )

    # --- Fetch Command ---
    parser_fetch = subparsers.add_parser(
        "fetch", help="Fetch and display your team's previous submissions and scores."
    )

    args = parser.parse_args()
    filepath = Path(getattr(args, "filepath", ""))

    # --- Command Logic ---
    if args.command == "validate":
        logger.info(f"--- 🔍 Validating file: {filepath} ---")
        try:
            submission_data = read_json(filepath)
            validate_submission_format(submission_data)
            logger.info("✅ Validation successful! The file format is correct.")
        except (FileNotFoundError, ValueError, RuntimeError) as e:
            logger.error(f"❌ Validation Failed: {e}")

    elif args.command == "submit":
        if args.dry_run:
            logger.info(f"--- 🌵 Performing a DRY RUN for file: {filepath} ---")
        else:
            logger.warning(f"--- 🚀 Performing a LIVE SUBMISSION for file: {filepath} ---")
            user_confirm = input("Are you sure you want to proceed? (yes/no): ")
            if user_confirm.lower() != 'yes':
                logger.info("Submission cancelled by user.")
                return

        try:
            submission_data = read_json(filepath)
            make_submission(submission_data, dry_run=args.dry_run, verbose=True)
            if args.dry_run:
                logger.info("✅ Dry run successful. The file is valid and ready to be submitted.")
        except (FileNotFoundError, ValueError, RuntimeError) as e:
            logger.error(f"❌ Submission Failed: {e}")

    elif args.command == "fetch":
        logger.info("--- 🚚 Fetching previous submissions... ---")
        try:
            submissions = fetch_my_submissions(verbose=True)
            if submissions:
                logger.info("--- 📋 Your Team's Submissions ---")
                print(json.dumps(submissions, indent=2, ensure_ascii=False))
            else:
                logger.info("No previous submissions found or the API call failed.")
        except RuntimeError as e:
            logger.error(f"❌ Failed to fetch submissions: {e}")


if __name__ == "__main__":
    main()