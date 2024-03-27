from unittest.mock import patch

from design_patterns.structural.facade_pattern.facade_pattern import *


class TestCar:
    @patch.object(ElectricalSystem, 'switch_on')
    @patch.object(IntakeSystem, 'open_throttle')
    @patch.object(FuelSystem, 'inject_fuel')
    @patch.object(IgnitionSystem, 'create_spark')
    def test_start_engine(self, mocked_create_spark, mocked_inject_fuel, mocked_open_throttle, mocked_switch_on):
        # Assign
        car = Car()

        # Act
        car.start_engine()

        # Assert
        """
        start_engine is a facade method that calls the subsystems
        """
        car.electrical_system.switch_on.assert_called_once()
        car.intake_system.open_throttle.assert_called_once()
        car.fuel_system.inject_fuel.assert_called_once()
        car.ignition_system.create_spark.assert_called_once()
