from design_patterns.structural.adapter_object_pattern.adapter_object_pattern import Car, GpsDeviceAdapter, GpsDevice, \
    Location


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
    gps_device = GpsDevice()
    gps_adapter = GpsDeviceAdapter(gps_device)

    # Act
    location = gps_adapter.get_location()

    # Assert
    assert isinstance(location, Location)


def test_car():
    """
    The client class uses the target interface via the adapter class.
    """
    # Assign
    gps_device = GpsDevice()
    gps_adapter = GpsDeviceAdapter(gps_device)
    car = Car(gps_adapter)

    # Act
    location = car.monitor_location()

    # Assert
    assert isinstance(location, Location)
