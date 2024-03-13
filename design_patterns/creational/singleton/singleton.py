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
    print("Car 1:", car1)

    # Attempt to get another reference to the car instance
    car2 = SingletonPattern.get_car()
    print("Car 2:", car2)

    # Check if both references point to the same car instance
    assert car1 is car2, "car1 and car2 are not the same instance"
    print("Are car1 and car2 the same instance?", car1 is car2)
