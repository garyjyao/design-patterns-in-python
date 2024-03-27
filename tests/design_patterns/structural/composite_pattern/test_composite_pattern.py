import uuid
from unittest.mock import MagicMock, patch
from design_patterns.structural.composite_pattern.composite_pattern import Leaf, Composite


def test_leaf():
    # Assign
    leaf = Leaf()

    with patch('builtins.print') as mocked_print:
        # Act
        leaf.operation()

        # Assert
        mocked_print.assert_called_once_with(f"operation on Leaf :{leaf.id}")


def test_composite_operation():
    """
    Test for Composite class' operation method, which calls the operation method of each leaf
    """
    # Assign
    leaf1 = MagicMock(Leaf)
    leaf1.id = uuid.uuid4()
    leaf2 = MagicMock(Leaf)
    leaf2.id = uuid.uuid4()

    composite = Composite([leaf1, leaf2])

    # Act
    composite.operation()

    # Assert
    leaf1.operation.assert_called_once()
    leaf2.operation.assert_called_once()
