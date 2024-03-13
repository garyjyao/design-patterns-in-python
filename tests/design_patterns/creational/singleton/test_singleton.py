from creational.singleton.creational.singleton.singleton import Car, SingletonPattern


def test_singleton_instance():
    car1: Car = SingletonPattern.get_car()
    car2: Car = SingletonPattern.get_car()
    assert car1 is car2, "Car instances are not the same"
