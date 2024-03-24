from design_patterns.creational.factorymethod_pattern.factorymethod_pattern import FactoryMethodPattern, Car, Truck


def test_create():
    # Arrange
    car_horn = "beep beep!"
    truck_horn = "honk honk!"

    # Act
    sedan = FactoryMethodPattern.create("sedan")
    truck = FactoryMethodPattern.create("truck")
    sedan_output = sedan.drive()
    truck_output = truck.drive()

    # Assert
    assert isinstance(sedan, Car), "Sedan should be a Car"
    assert isinstance(truck, Truck), "Truck should be a Truck"
    assert sedan_output == car_horn, "Car horn is not correct"
    assert truck_output == truck_horn, "Truck horn is not correct"


def test_create_unknown_type():
    # Arrange
    unknown_type = "unknown"

    # Act / Assert
    try:
        FactoryMethodPattern.create(unknown_type)
        assert False, "Unknown vehicle type should raise a ValueError"
    except ValueError as e:
        assert str(e) == "Unknown vehicle type", "Unknown vehicle type should raise a ValueError"

