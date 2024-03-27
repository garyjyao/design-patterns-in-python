from unittest.mock import MagicMock
from design_patterns.structural.adapter_class_pattern.adapter_class_pattern import GpsDeviceAdapter, Car, Location, GpsDevice


def test_gps_device():
    """
    The adaptee class has a different interface than the target interface.
    """
    # Assign
    gps_device = GpsDevice()

    # Act
    location = gps_device.get_location()

    # Assert
    assert isinstance(location, Location)


def test_gps_device_adapter():
    """
    The adapter class adapts the interface of the adaptee class to the target interface.
    """
    # Assign
    # Create a mock for the GpsDeviceAdapter
    mock_adapter = MagicMock(GpsDeviceAdapter)
    mock_adapter.get_location.return_value = Location()

    # Create a Car instance with the mock adapter
    car = Car(mock_adapter)

    # Act
    # Call the monitor_location method (target interface method)
    location = car.monitor_location()

    # Assert
    # Assert that the get_location method was called (adaptee method)
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
