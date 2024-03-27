from unittest.mock import patch, call

from design_patterns.structural.decorator_pattern.decorator_pattern import *


@patch.object(Cylinder, 'operate')
@patch.object(TemperatureSensingComponent, 'measure_temperature')
def test_decorator_pattern(mocked_measure_temperature, mocked_cylinder_operate):
    """
    Test for Decorator class' method decorate the Concrete Component method
    """
    # Assign
    component = Cylinder()
    temperature_sensing_component = TemperatureSensingComponent(component)

    # Act
    temperature_sensing_component.operate()

    # Assert
    mocked_cylinder_operate.assert_called_once()
    mocked_measure_temperature.assert_has_calls([call("before"), call("after")])


def test_cylinder():
    """
    Test for Concrete Class
    """
    # Assign
    component = Cylinder()

    # Act
    component.get_name()
    component.operate()

    # Assert (Nothing went wrong)
    assert True


def test_temperature_sensing_component():
    """
    Test for Decorator Class
    """
    # Assign
    component = Cylinder()
    temperature_sensing_component = TemperatureSensingComponent(component)

    # Act
    temperature_sensing_component.get_name()
    temperature_sensing_component.operate()

    # Assert (Nothing went wrong)
    assert True
