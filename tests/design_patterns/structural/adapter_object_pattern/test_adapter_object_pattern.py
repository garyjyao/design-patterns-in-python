from design_patterns.structural.adapter_object_pattern.adapter_object_pattern import Car, GpsDeviceAdapter, GpsDevice, \
    Location


def test_gps_device():
    gps_device = GpsDevice()
    location = gps_device.get_location()
    assert isinstance(location, Location)


def test_gps_device_adapter():
    gps_device = GpsDevice()
    gps_adapter = GpsDeviceAdapter(gps_device)
    location = gps_adapter.get_location()
    assert isinstance(location, Location)


def test_car():
    gps_device = GpsDevice()
    gps_adapter = GpsDeviceAdapter(gps_device)
    car = Car(gps_adapter)
    location = car.monitor_location()
    assert isinstance(location, Location)
