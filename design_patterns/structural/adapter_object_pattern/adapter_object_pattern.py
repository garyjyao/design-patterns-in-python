class Location:
    pass


class GpsDevice:
    def get_location(self):
        return Location()


class GpsDeviceAdapter:
    def __init__(self, gps_device):
        self.gps_device = gps_device

    def get_location(self):
        return self.gps_device.get_location()


class Car:
    def __init__(self, adapter):
        self.adapter = adapter

    def monitor_location(self):
        return self.adapter.get_location()


if __name__ == "__main__":
    car = Car(GpsDeviceAdapter(GpsDevice()))
    car.monitor_location()
