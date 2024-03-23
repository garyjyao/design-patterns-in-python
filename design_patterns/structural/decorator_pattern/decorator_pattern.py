from abc import ABC, abstractmethod
from typing import override


class EngineComponent(ABC):
    @abstractmethod
    def operate(self):
        raise NotImplementedError


class Cylinder(EngineComponent):
    @override
    def operate(self):
        pass


class TemperatureSensingComponent(EngineComponent):
    def __init__(self, component):
        self.component = component
        self.location = "Engine"

    def measure_temperature(self, message):
        print(f"Measuring temperature at '{self.location}' {message}")

    def operate(self):
        self.measure_temperature("before")
        self.component.operate()
        self.measure_temperature("after")


if __name__ == "__main__":
    cylinder = Cylinder()
    temperature_sensing_cylinder = TemperatureSensingComponent(cylinder)
    temperature_sensing_cylinder.operate()
