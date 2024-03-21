from abc import ABC, abstractmethod


class CarElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError


class CarElementVisitor(ABC):
    @abstractmethod
    def visit(self, element):
        raise NotImplementedError


class Car(CarElement):
    def __init__(self):
        self.elements = [Body(), Engine(), Wheel()]

    def accept(self, visitor):
        names = []
        for element in self.elements:
            name = element.accept(visitor)
            names.append(name)
        visitor.visit(self)
        names.append('Car')
        return names


class Wheel(CarElement):
    def accept(self, visitor):
        visitor.visit(self)
        return 'Wheel'


class Engine(CarElement):
    def accept(self, visitor):
        visitor.visit(self)
        return 'Engine'


class Body(CarElement):
    def accept(self, visitor):
        visitor.visit(self)
        return 'Body'


class CarElementDoVisitor(CarElementVisitor):
    def visit(self, element):
        print(f"Visiting {element.__class__.__name__}")
        return element.__class__.__name__


if __name__ == "__main__":
    car = Car()
    car.accept(CarElementDoVisitor())
    # try to extend this example with another visitor like CarElementPriceVisitor for calculate price of each element
    # try to extend this example with another element like Window
