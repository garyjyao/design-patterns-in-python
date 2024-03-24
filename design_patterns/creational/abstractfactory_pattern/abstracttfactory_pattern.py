from abc import ABC, abstractmethod
from typing import override


# Engine interface
class Engine(ABC):
    @abstractmethod
    def __str__(self):
        pass


# PetrolEngine class implementing Engine
class PetrolEngine(Engine):
    def __str__(self):
        return "Petrol Engine"


# DieselEngine class implementing Engine
class DieselEngine(Engine):
    def __str__(self):
        return "Diesel Engine"


class EngineFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass


class CarEngineFactory(EngineFactory):
    @override
    def create_engine(self):
        return PetrolEngine()


class TruckEngineFactory(EngineFactory):
    @override
    def create_engine(self):
        return DieselEngine()


class EngineFactoryFactory:
    @staticmethod
    def create_factory(engine_type):
        if engine_type == "car":
            return CarEngineFactory()
        if engine_type == "truck":
            return TruckEngineFactory()
        # else:
        raise ValueError("Unknown factory type")


# For java, everything is wrapped in a class
# class AbstractFactoryPattern:
#     @staticmethod
#     def main():
#         vehicle = input("What type of vehicle will you be driving today, car or truck?")
#         factory = EngineFactoryFactory.create_factory(vehicle)
#         engine = factory.create_engine()
#         print(engine)

# if __name__ == "__main__":
#     AbstractFactoryPattern.main()

# Demonstrate of the abstract factory pattern without creating wrapping class
if __name__ == "__main__":
    vehicle = input("What type of vehicle will you be driving today, car or truck?")
    factory = EngineFactoryFactory.create_factory(vehicle)
    engine = factory.create_engine()
    print(engine)
