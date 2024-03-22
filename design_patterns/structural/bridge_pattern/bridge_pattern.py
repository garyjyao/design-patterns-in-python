from abc import abstractmethod, ABC
from typing import override


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        raise NotImplementedError


class FileLogger(Logger):
    @override
    def log(self, message):
        print(f"FILE {message}")


class ConsoleLogger(Logger):
    @override
    def log(self, message):
        print(f"CONSOLE {message}")


class BankAccount:
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
    account.set_logger(ConsoleLogger())
    account.withdraw(100)
