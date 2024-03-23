import uuid
from unittest.mock import MagicMock, patch
from design_patterns.structural.composite_pattern.composite_pattern import Leaf, Composite


def test_leaf():
    # Create a Leaf instance
    leaf = Leaf()

    # Mock the print function
    with patch('builtins.print') as mocked_print:
        # Call the operation method
        leaf.operation()

        # Assert that print was called with the expected argument
        mocked_print.assert_called_once_with(f"operation on Leaf :{leaf.id}")


def test_composite_operation():
    # Create mock Leaf instances
    leaf1 = MagicMock(Leaf)
    leaf1.id = uuid.uuid4()
    leaf2 = MagicMock(Leaf)
    leaf2.id = uuid.uuid4()

    # Create a Composite instance with the mock Leaf instances
    composite = Composite([leaf1, leaf2])

    # Call the operation method
    composite.operation()

    # Assert that the operation method was called on each Leaf instance
    leaf1.operation.assert_called_once()
    leaf2.operation.assert_called_once()
