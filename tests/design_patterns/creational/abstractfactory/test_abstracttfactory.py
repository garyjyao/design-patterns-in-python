import pytest

from design_patterns.creational.abstractfactory.abstracttfactory import EngineFactoryFactory, PetrolEngine, DieselEngine


def test_known_engine_type():
    # Assign

    # Act
    car_factory = EngineFactoryFactory.create_factory("car")
    truck_factory = EngineFactoryFactory.create_factory("truck")
    car_engine = car_factory.create_engine()
    truck_engine = truck_factory.create_engine()

    # Assert
    assert isinstance(car_engine, PetrolEngine)
    assert isinstance(truck_engine, DieselEngine)
    assert str(car_engine) == "Petrol Engine"
    assert str(truck_engine) == "Diesel Engine"


def test_unknown_engine_type():
    # Assign
    # Act
    # Assert
    with pytest.raises(ValueError) as e:
        telsa_factory = EngineFactoryFactory.create_factory("telsa")

    assert str(e.value) == "Unknown factory type"

