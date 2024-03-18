from design_patterns.behavioral.iterator.iterator import *


def test_range_iterator():
    # Assign
    range_iterator = RangeIterator(0, 10)

    # Act
    iterator_order = [i for i in range_iterator]

    # Assert
    assert iterator_order == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]