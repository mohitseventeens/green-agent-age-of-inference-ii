import logging
from pocketflow import Node
from src.utils.data_retrieval import load_all_data

# --- Set up logging for the module ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class LoadStaticDataNode(Node):
    """
    A node that loads all job and training data from local markdown files
    into the shared store at the beginning of a flow.
    """
    def prep(self, shared):
        """
        This node is a data source and does not require any input from the shared store.
        """
        return None # Explicitly return None as there's nothing to prepare.

    def exec(self, prep_res):
        """
        Calls the data_retrieval utility to load data from the file system.
        """
        logger.info("Loading all static data (jobs and trainings)...")
        jobs = load_all_data("jobs")
        trainings = load_all_data("trainings")
        return {"jobs": jobs, "trainings": trainings}
        
    def post(self, shared, prep_res, exec_res):
        """
        Populates the shared store with the loaded data.
        """
        shared["all_jobs"] = exec_res.get("jobs", [])
        shared["all_trainings"] = exec_res.get("trainings", [])
        logger.info(f"Loaded {len(shared['all_jobs'])} jobs and {len(shared['all_trainings'])} trainings into shared store.")
        # No action needed for flow control, so we return None (or nothing)
