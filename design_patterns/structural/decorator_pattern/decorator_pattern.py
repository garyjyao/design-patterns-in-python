from abc import ABC, abstractmethod
from typing import override


class EngineComponent(ABC):
    """
    The Component interface declares the common interface for all concrete components, both simple and decorated.
    """
    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def operate(self):
        raise NotImplementedError


class Cylinder(EngineComponent):
    """
    Concrete Components provide default implementations of the operations.
    """
    @override
    def get_name(self):
        return "Cylinder"

    @override
    def operate(self):
        pass


class TemperatureSensingComponent(EngineComponent):
    """
    This is a Decorator class.
    The TemperatureSensingComponent class is a decorator that also implements the EngineComponent interface.
    It has an instance variable component which holds the reference to the object it decorates.
    It overrides the operate method to add new behavior before and after the operate method of the decorated object.
    """
    def __init__(self, component):
        self.component = component

    def get_name(self):
        pass

    def measure_temperature(self, message):
        print(f"Measuring temperature at '{self.component.get_name()}' {message}")

    def operate(self):

        self.measure_temperature("before")
        self.component.operate()
        self.measure_temperature("after")


if __name__ == "__main__":
    cylinder = Cylinder()
    temperature_sensing_cylinder = TemperatureSensingComponent(cylinder)
    """
    The Decorator pattern is a structural design pattern that allows behavior to be added to an individual object,
    either statically or dynamically, without affecting the behavior of other objects from the same class.
    The operate method of the TemperatureSensingComponent class adds new behavior before and after the operate method.
    """
    temperature_sensing_cylinder.operate()
