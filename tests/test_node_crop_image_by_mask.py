#!/usr/bin/env python

"""Tests for `node_crop_image_by_mask` package."""

import pytest
from src.node_crop_image_by_mask.nodes import MaskCropperNode

@pytest.fixture
def example_node():
    """Fixture to create an Example node instance."""
    return MaskCropperNode()

def test_example_node_initialization(example_node):
    """Test that the node can be instantiated."""
    assert isinstance(example_node, MaskCropperNode)

def test_return_types():
    """Test the node's metadata."""
    assert MaskCropperNode.RETURN_TYPES == ("IMAGE",)
    assert MaskCropperNode.FUNCTION == "test"
    assert MaskCropperNode.CATEGORY == "Example"
