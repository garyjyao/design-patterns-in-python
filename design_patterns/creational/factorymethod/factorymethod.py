# Demonstrate the factory method pattern
from abc import ABC, abstractmethod
from typing import override


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        # drive method is abstract and must be implemented by subclasses
        pass


class Car(Vehicle):
    @override
    def drive(self):
        print("Driving a car.")
        return "beep beep!"


class Truck(Vehicle):
    @override
    def drive(self):
        print("Driving a truck.")
        return "honk honk!"


class FactoryMethodPattern:
    @staticmethod
    def create(vehicle_type):
        if vehicle_type == "sedan":
            return Car()
        if vehicle_type == "truck":
            return Truck()
        raise ValueError("Unknown vehicle type")


# main method is just a simple demonstration of how pattern can be invoked, no really meaning
if __name__ == "__main__":
    sedan = FactoryMethodPattern.create("sedan")
    truck = FactoryMethodPattern.create("truck")
    sedan.drive()
    truck.drive()
