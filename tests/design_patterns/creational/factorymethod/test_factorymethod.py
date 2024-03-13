from design_patterns.creational.factorymethod.factorymethod import FactoryMethodPattern


def test_create():
    # Arrange
    car_horn = "beep beep!"
    truck_horn = "honk honk!"
    sedan = FactoryMethodPattern.create("sedan")
    truck = FactoryMethodPattern.create("truck")

    # Act
    sedan_output = sedan.drive()
    truck_output = truck.drive()

    # Assert
    assert sedan_output == car_horn, "Car horn is not correct"
    assert truck_output == truck_horn, "Truck horn is not correct"


