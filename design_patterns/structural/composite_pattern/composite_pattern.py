import uuid
from abc import ABC, abstractmethod
from typing import override


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    def __init__(self):
        self.id = uuid.uuid4()

    @override
    def operation(self):
        print(f"operation on Leaf :{self.id}")


class Composite(Component):
    def __init__(self, children):
        self.children = children

    def operation(self):
        for child in self.children:
            child.operation()


if __name__ == "__main__":
    leaf1 = Leaf()
    leaf2 = Leaf()
    leaf3 = Leaf()
    leaf4 = Leaf()
    c1 = Composite([leaf1, leaf2])
    c2 = Composite([leaf3, leaf4])
    main_leaf = Composite([c1, c2])
    main_leaf.operation()
