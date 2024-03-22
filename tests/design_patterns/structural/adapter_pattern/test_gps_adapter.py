from unittest.mock import MagicMock
from design_patterns.structural.adapter_pattern.gps_adapter import GpsDeviceAdapter, Car, Location, GpsDevice


def test_gps_device():
    # Assign
    gps_device = GpsDevice()

    # Act
    location = gps_device.get_location()

    # Assert
    assert isinstance(location, Location)


def test_gps_device_adapter():
    # Assign
    # Create a mock for the GpsDeviceAdapter
    mock_adapter = MagicMock(GpsDeviceAdapter)
    mock_adapter.get_location.return_value = Location()

    # Create a Car instance with the mock adapter
    car = Car(mock_adapter)

    # Act
    # Call the monitor_location method
    location = car.monitor_location()

    # Assert
    # Assert that the get_location method was called
    mock_adapter.get_location.assert_called_once()

    # Assert that the returned location is an instance of Location
    assert isinstance(location, Location)


def test_car():
    # Assign
    car = Car(GpsDeviceAdapter())

    # Act
    location = car.monitor_location()

    # Assert
    assert isinstance(location, Location)
