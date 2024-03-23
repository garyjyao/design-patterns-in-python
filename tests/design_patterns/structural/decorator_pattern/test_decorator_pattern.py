from unittest.mock import patch, call

from design_patterns.structural.decorator_pattern.decorator_pattern import *


@patch.object(Cylinder, 'operate')
@patch.object(TemperatureSensingComponent, 'measure_temperature')
def test_decorator_pattern(mocked_measure_temperature, mocked_cylinder_operate):
    # Assign
    component = Cylinder()
    temperature_sensing_component = TemperatureSensingComponent(component)

    # Act
    temperature_sensing_component.operate()

    # Assert
    mocked_cylinder_operate.assert_called_once()
    mocked_measure_temperature.assert_has_calls([call("before"), call("after")])
