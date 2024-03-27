class Location:
    pass


class GpsDevice:
    """
    The adaptee class has a different interface than the target interface.
    """

    def get_location(self):
        return Location()


class GpsDeviceAdapter(GpsDevice):
    """
    The adapter class adapts the interface of the adaptee class to the target interface using inheritance.
    """

    def get_location(self):  # pylint: disable=useless-super-delegation
        return super().get_location()


class Car:
    def __init__(self, adapter):
        self.adapter = adapter

    def monitor_location(self):
        """
        The client class uses the target interface via the adapter class.
        """
        location = self.adapter.get_location()
        return location


if __name__ == "__main__":
    # Car only know a method called monitor_location,
    # but it doesn't know how to get the location using the GpsDevice class.
    # The adapter class GpsDeviceAdapter is used to adapt the GpsDevice class
    # to the Car class.
    car = Car(GpsDeviceAdapter())
    car.monitor_location()
