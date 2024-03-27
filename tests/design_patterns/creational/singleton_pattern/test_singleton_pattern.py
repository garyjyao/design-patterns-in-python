from design_patterns.creational.singleton_pattern.singleton_pattern import Car, SingletonPattern


def test_singleton_instance():
    # Assign

    # Act
    car1: Car = SingletonPattern.get_car()
    car2: Car = SingletonPattern.get_car()

    # Assert
    assert car1 is car2, "Car instances are not the same"
