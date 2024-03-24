from design_patterns.behavioral.iterator_pattern.name_repository_iterator import *


def test_name_repository_iterator_using_while_loop():
    # Assign
    names = ["Robert", "John","Julie", "Lora"]
    name_repository_iterator = NameRepositoryIterator(names)

    # Act
    iterator_order = []
    # using while loop with has_next and next methods
    while name_repository_iterator.has_next():
        iterator_order.append(name_repository_iterator.next())

    # Assert
    assert iterator_order == ["Robert", "John","Julie", "Lora"]

def test_name_repository_iterator_using_for_loop():
    # Assign
    names = ["Robert", "John","Julie", "Lora"]
    name_repository_iterator = NameRepositoryIterator(names)

    # Act
    iterator_order = []
    # using for loop with __iter__ and __next__ methods
    iterator_order = [name for name in name_repository_iterator]

    # Assert
    assert iterator_order == ["Robert", "John","Julie", "Lora"]
