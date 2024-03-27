"""
Let's consider a scenario where we have an existing class named 'OldPrinter'.
This class has a method named 'print_old()' which prints messages using an old mechanism.
In our new system, we expect objects of type 'Printer' with a 'print()' method.
To bridge this gap, we introduce a 'ModernPrinter' class that directly implements the 'Printer' interface
with a 'print()' method. The 'ModernPrinter' class uses an instance of the 'OldPrinter' class to print messages.
This is achieved by creating an adapter class named 'OldPrinterAdapter' that implements the 'Printer' interface
and uses an instance of the 'OldPrinter' class to print messages.
The 'ModernPrinter' class uses an instance of the 'OldPrinterAdapter' class to print messages.
This way, the 'ModernPrinter' class can use the 'OldPrinter' class to print messages without any changes
to the 'OldPrinter' class.
"""
from abc import ABC, abstractmethod
from typing import override


# Target interface
class Printer(ABC):
    """
    The Target interface is the interface that the client code expects to work with.
    """

    @abstractmethod
    def print(self, message):
        raise NotImplementedError


# Adaptee class
class OldPrinter:
    """
    The Adaptee class is an existing class that has a different interface from the target interface.
    """

    def print_old(self, message):
        print(f"Old Printer: {message}")


# Adapter class
class PrinterAdapter(Printer):
    """
    The Adapter class owns an instance of the Adaptee class and implements the target interface using that instance.
    """

    def __init__(self, old_printer):
        self.old_printer = old_printer

    @override
    def print(self, message):
        """
        The Adapter class implements the target interface and uses the Adaptee class to perform the desired action.
        """
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
