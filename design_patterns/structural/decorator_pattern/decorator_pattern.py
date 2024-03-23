from abc import ABC, abstractmethod
from typing import override


class EngineComponent(ABC):
    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def operate(self):
        raise NotImplementedError


class Cylinder(EngineComponent):
    @override
    def get_name(self):
        return "Cylinder"

    @override
    def operate(self):
        pass


class TemperatureSensingComponent(EngineComponent):
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
    temperature_sensing_cylinder.operate()
