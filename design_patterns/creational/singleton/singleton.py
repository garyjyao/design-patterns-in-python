class Car:
    pass


class SingletonPattern:
    _car_instance = Car()

    @staticmethod
    def get_car():
        return SingletonPattern._car_instance


if __name__ == "__main__":
    # Get a reference to the car instance
    car1 = SingletonPattern.get_car()

    # Attempt to get another reference to the car instance
    car2 = SingletonPattern.get_car()

    # Check if both references point to the same car instance
    assert car1 is car2, "car1 and car2 are not the same instance"
