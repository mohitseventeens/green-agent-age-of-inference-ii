import pytest
from src.nodes import LoadStaticDataNode

def test_load_static_data_node():
    """
    Tests that the LoadStaticDataNode correctly loads jobs and trainings
    and populates the shared store.
    """
    # Arrange
    node = LoadStaticDataNode()
    shared = {} # Start with an empty shared store

    # Act
    node.run(shared)

    # Assert
    # Check that the data exists in the shared store
    assert "all_jobs" in shared
    assert "all_trainings" in shared

    # Check the types and lengths
    assert isinstance(shared["all_jobs"], list)
    assert isinstance(shared["all_trainings"], list)
    assert len(shared["all_jobs"]) == 200
    assert len(shared["all_trainings"]) == 497

    # Check the content of a sample item from each list
    assert "id" in shared["all_jobs"][0]
    assert "content" in shared["all_jobs"][0]
    assert shared["all_jobs"][0]["id"] == "j0"

    assert "id" in shared["all_trainings"][0]
    assert "content" in shared["all_trainings"][0]
    assert shared["all_trainings"][0]["id"] == "tr0"
