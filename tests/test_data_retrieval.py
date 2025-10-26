import pytest
from src.utils.data_retrieval import load_all_data

def test_load_all_data_for_jobs():
    """
    Tests that job data is loaded correctly into the expected format.
    """
    # Act
    jobs_data = load_all_data("jobs")

    # Assert
    assert isinstance(jobs_data, list), "Should return a list."
    assert len(jobs_data) == 200, "Should load all 200 job files."
    
    # Check the structure of the first item
    first_job = jobs_data[0]
    assert isinstance(first_job, dict), "Each item in the list should be a dict."
    assert "id" in first_job, "Each dict should have an 'id' key."
    assert "content" in first_job, "Each dict should have a 'content' key."
    assert first_job['id'] == 'j0', "The ID should be derived from the filename."
    assert len(first_job['content']) > 50, "Content should not be empty."

def test_load_all_data_for_trainings():
    """
    Tests that training data is loaded correctly into the expected format.
    """
    # Act
    trainings_data = load_all_data("trainings")

    # Assert
    assert isinstance(trainings_data, list), "Should return a list."
    assert len(trainings_data) == 497, "Should load all 497 training files."
    
    # Check the structure of the first item
    first_training = trainings_data[0]
    assert isinstance(first_training, dict), "Each item should be a dict."
    assert "id" in first_training, "Each dict should have an 'id' key."
    assert "content" in first_training, "Each dict should have a 'content' key."
    assert first_training['id'] == 'tr0', "The ID should be derived from the filename."
    assert len(first_training['content']) > 50, "Content should not be empty."

def test_load_all_data_with_invalid_type():
    """
    Tests that the function handles an invalid data_type gracefully.
    This test expects a FileNotFoundError or similar, which results in an empty list.
    """
    # Act
    invalid_data = load_all_data("non_existent_type")

    # Assert
    assert isinstance(invalid_data, list), "Should return a list even on error."
    assert len(invalid_data) == 0, "Should return an empty list for invalid types."
