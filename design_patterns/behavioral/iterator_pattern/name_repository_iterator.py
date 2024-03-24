from abc import ABC, abstractmethod
from typing import override


class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class Container(ABC):
    @abstractmethod
    def get_iterator(self):
        pass


class NameRepositoryIterator(Iterator):
    def __init__(self, names):
        self.names = names
        self.index = 0

    @override
    def has_next(self):
        return self.index < len(self.names)

    @override
    def next(self):
        if self.has_next():
            name = self.names[self.index]
            self.index += 1
            return name
        return None

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_next():  # pylint: disable=no-else-return
            name = self.names[self.index]
            self.index += 1
            return name
        else:
            raise StopIteration

# if __name__ == "__main__":
#     names = ["Robert", "John","Julie", "Lora"]
#     name_repository_iterator = NameRepositoryIterator(names)
#     # using while loop with has_next and next methods
#     while name_repository_iterator.has_next():
#         print(name_repository_iterator.next(), end=" ")
#     # using for loop with __iter__ and __next__ methods
#     name_repository_iterator = NameRepositoryIterator(names)
#     for name in name_repository_iterator:
#         print(name, end=" ")
