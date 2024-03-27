class Location:
    pass


class GpsDevice:
    """
    The Adaptee class, which has a different interface than the Target interface.
    """

    def get_location(self):
        return Location()


class GpsDeviceAdapter:
    """
    The Adapter class, which adapts the interface of the Adaptee class to the Target interface using composite.
    """

    def __init__(self, gps_device):
        self.gps_device = gps_device

    def get_location(self):
        return self.gps_device.get_location()


class Car:
    """
    The Client class, which uses the Target interface.
    """

    def __init__(self, adapter):
        self.adapter = adapter

    def monitor_location(self):
        """
        The target interface method that the client code expects to work with.
        """
        return self.adapter.get_location()


if __name__ == "__main__":
    car = Car(GpsDeviceAdapter(GpsDevice()))
    car.monitor_location()
