from abc import ABC, abstractmethod
from typing import override


# Target interface
class Printer(ABC):
    @abstractmethod
    def print(self, message):
        raise NotImplementedError


# Adaptee class
class OldPrinter:
    def print_old(self, message):
        print(f"Old Printer: {message}")


# Adapter class
class PrinterAdapter(Printer):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    @override
    def print(self, message):
        self.old_printer.print_old(message)


# New implementation of the Printer interface
class ModernPrinter(Printer):
    @override
    def print(self, message):
        print(f"Modern Printer: {message}")


# Client code
if __name__ == "__main__":
    # Create an instance of the adapter
    printer_adapter = PrinterAdapter(OldPrinter())

    # Use the new interface to print a message with the old printer
    printer_adapter.print("Hello, Adapter Pattern with Old Printer!")

    # Create an instance of the ModernPrinter
    modern_printer = ModernPrinter()

    # Use the new interface to print a message with the modern printer
    modern_printer.print("Hello, from Modern Printer!")
