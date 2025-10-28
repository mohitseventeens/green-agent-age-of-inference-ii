# src/flow.py

import logging
from pocketflow import Flow
from src.nodes import (
    LoadStaticDataNode,
    ParseStaticDataNode,
    ExtractProfileNode,
    DecisionNode,
    ProvideAwarenessNode,
    FindTrainingsOnlyNode,
    FindJobsAndTrainingsNode,
    FinalizeOutputNode,
)

# --- Set up logging ---
logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def create_main_flow() -> Flow:
    """
    Instantiates all nodes and assembles them into the main PocketFlow workflow.

    Returns:
        The fully constructed main flow, ready to be executed.
    """
    logger.info("Creating the main application flow...")

    # 1. Instantiate all nodes
    load_static_data_node = LoadStaticDataNode()
    parse_static_data_node = ParseStaticDataNode()
    extract_profile_node = ExtractProfileNode()
    decision_node = DecisionNode()

    parse_static_data_node.set_params({
    "parsing_model": "mistral-large-latest"
})
    
    # Branch nodes
    provide_awareness_node = ProvideAwarenessNode()
    find_trainings_only_node = FindTrainingsOnlyNode()
    
    # Configure the jobs/trainings node to use the powerful model for scoring
    find_jobs_and_trainings_node = FindJobsAndTrainingsNode()
    find_jobs_and_trainings_node.set_params({
        "use_cache_for_scoring": True, # Use cache in production for speed/cost
        "scoring_model": "mistral-large-latest"
    })
    
    # Final output node
    finalize_output_node = FinalizeOutputNode()

    # 2. Connect the nodes into a workflow
    
    # Linear pre-processing chain
    load_static_data_node >> parse_static_data_node >> extract_profile_node >> decision_node
    
    # Conditional branching from the decision node
    (decision_node - "provide_awareness_young") >> provide_awareness_node
    (decision_node - "provide_awareness_info") >> provide_awareness_node
    (decision_node - "recommend_trainings") >> find_trainings_only_node
    (decision_node - "recommend_jobs") >> find_jobs_and_trainings_node

    # All branches converge on the finalize output node
    provide_awareness_node >> finalize_output_node
    find_trainings_only_node >> finalize_output_node
    find_jobs_and_trainings_node >> finalize_output_node

    # 3. Create and return the Flow object, specifying the start node
    main_flow = Flow(start=load_static_data_node)
    
    logger.info("Main flow created successfully.")
    return main_flow