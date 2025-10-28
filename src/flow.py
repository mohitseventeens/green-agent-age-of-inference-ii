# src/flow.py
import logging
from pocketflow import Flow
from src.nodes import (
    DecisionNode,
    ProvideAwarenessNode,
    FindTrainingsOnlyNode,
    FindJobsAndTrainingsNode,
    FinalizeOutputNode,
    # No longer need ExtractProfileNode here
)

logger = logging.getLogger(__name__)
# (logging setup remains the same)

def create_recommendation_flow() -> Flow:
    """
    Assembles the workflow that starts AFTER a persona profile is already known.
    """
    logger.info("Creating the recommendation-only flow...")

    # Instantiate nodes
    decision_node = DecisionNode()
    provide_awareness_node = ProvideAwarenessNode()
    find_trainings_only_node = FindTrainingsOnlyNode()
    find_jobs_and_trainings_node = FindJobsAndTrainingsNode()
    finalize_output_node = FinalizeOutputNode()

    # Configure the jobs node for high-quality scoring
    find_jobs_and_trainings_node.set_params({
        "use_cache_for_scoring": True,
        "scoring_model": "mistral-large-latest"
    })
    
    # Connect nodes
    (decision_node - "provide_awareness_young") >> provide_awareness_node
    (decision_node - "provide_awareness_info") >> provide_awareness_node
    (decision_node - "recommend_trainings") >> find_trainings_only_node
    (decision_node - "recommend_jobs") >> find_jobs_and_trainings_node

    provide_awareness_node >> finalize_output_node
    find_trainings_only_node >> finalize_output_node
    find_jobs_and_trainings_node >> finalize_output_node

    # The flow now starts with the DecisionNode
    rec_flow = Flow(start=decision_node)
    
    logger.info("Recommendation-only flow created successfully.")
    return rec_flow