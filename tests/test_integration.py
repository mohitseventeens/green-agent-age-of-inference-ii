# tests/test_integration.py

import pytest
from pocketflow import Flow
from src.flow import create_main_flow
from src.nodes import LoadStaticDataNode, ParseStaticDataNode

def test_flow_creation_and_structure():
    """
    Tests that the main flow is created without errors and that the
    initial nodes are connected correctly.
    """
    # Act
    flow = create_main_flow()

    # Assert
    assert isinstance(flow, Flow), "The factory should return a Flow object."
    assert flow.start_node is not None, "The flow must have a start node."
    assert isinstance(flow.start_node, LoadStaticDataNode), "The start node is incorrect."
    
    # Check the connection of the first two nodes
    successor = flow.start_node.successors.get("default")
    assert successor is not None, "The first node should have a default successor."
    assert isinstance(successor, ParseStaticDataNode), "The connection to the second node is incorrect."