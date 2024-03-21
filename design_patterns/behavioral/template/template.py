from abc import ABC, abstractmethod
from typing import override


class SomeClass(ABC):
    def workflow(self):
        s = self.get_component1() + self.get_component2() + self.some_local_method()
        print(s)
        return s

    def some_local_method(self):
        return "local_method"

    @abstractmethod
    def get_component1(self):
        raise NotImplementedError

    @abstractmethod
    def get_component2(self):
        raise NotImplementedError


class ConcreteClass1(SomeClass):
    @override
    def get_component1(self):
        return "component1"

    @override
    def get_component2(self):
        return "component2"


if __name__ == "__main__":
    # get_component1(), get_component2() and some_local_method() are called in order defined by the template workflow()
    ConcreteClass1().workflow()
