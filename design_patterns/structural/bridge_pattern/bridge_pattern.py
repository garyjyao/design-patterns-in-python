from abc import abstractmethod, ABC
from typing import override


class Logger(ABC):
    """
    The Logger interface declares the operations that all concrete loggers must implement.
    It is one dimension of the bridge pattern.
    """

    @abstractmethod
    def log(self, message):
        raise NotImplementedError


class FileLogger(Logger):
    """
    The FileLogger class is one of the concrete loggers, evolved from the Logger interface.
    """

    @override
    def log(self, message):
        print(f"FILE {message}")


class ConsoleLogger(Logger):
    """
    The ConsoleLogger class is one of the concrete loggers, evolved from the Logger interface.
    """

    @override
    def log(self, message):
        print(f"CONSOLE {message}")


class BankAccount:
    """
    The BankAccount class is the other object, evolved independently of Logger object.
    """

    def __init__(self):
        self.logger = FileLogger()

    def withdraw(self, amount):
        self.logger.log(f"withdraw {amount}")

    def deposit(self, amount):
        self.logger.log(f"deposit {amount}")

    def set_logger(self, logger):
        self.logger = logger


if __name__ == "__main__":
    account = BankAccount()
    account.deposit(100)
    # Logger Class change does not affect the BankAccount class
    account.set_logger(ConsoleLogger())
    account.withdraw(100)
