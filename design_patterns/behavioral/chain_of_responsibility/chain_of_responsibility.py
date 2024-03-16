# Demonstrate chain of responsibility pattern
from abc import ABC, abstractmethod


class Request:
    pass


class AbstractProcessor(ABC):
    def __init__(self, next_processor=None):
        self._next_processor = next_processor

    @abstractmethod
    def process(self, request: Request):
        raise NotImplementedError


class DefaultProcessor(AbstractProcessor):
    # Python will automatically call the parent class's __init__ method if there is no __init__ method in the subclass
    # def __init__(self, next_processor=None):
    #     super().__init__(next_processor)

    def process(self, request: Request):
        print("Processing request by default processor")
        if self._next_processor:
            self._next_processor.process(request)


class SomeOtherProcessor(AbstractProcessor):
    # Python will automatically call the parent class's __init__ method if there is no __init__ method in the subclass
    # def __init__(self, next_processor=None):
    #     super().__init__(next_processor)

    def process(self, request: Request):
        print("Processing request by some other processor")
        if self._next_processor:
            self._next_processor.process(request)


if __name__ == "__main__":
    some_other_processor = SomeOtherProcessor()
    default_processor = DefaultProcessor(some_other_processor)
    default_processor.process(Request())
    # Output:
    #   Processing request by default processor
    #   Processing request by some other processor
