class Location:
    pass


class GpsDevice:
    def get_location(self):
        return Location()


class GpsDeviceAdapter(GpsDevice):
    def get_location(self):  # pylint: disable=useless-super-delegation
        return super().get_location()


class Car:
    def __init__(self, adapter):
        self.adapter = adapter

    def monitor_location(self):
        location = self.adapter.get_location()
        return location


if __name__ == "__main__":
    # Car only know a method called monitor_location,
    # but it doesn't know how to get the location using the GpsDevice class.
    # The adapter class GpsDeviceAdapter is used to adapt the GpsDevice class
    # to the Car class.
    car = Car(GpsDeviceAdapter())
    car.monitor_location()
