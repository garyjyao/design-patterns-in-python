Let's consider a scenario where we have an existing class named 'OldPrinter'. This class has a method named 'print_old()'
which prints messages using an old mechanism. In our new system, we expect objects of type 'Printer' with a 'print()' method.
To bridge this gap, we introduce a 'ModernPrinter' class that directly implements the 'Printer' interface with a 'print()' method.
The 'ModernPrinter' class uses an instance of the 'OldPrinter' class to print messages. This is achieved by creating an adapter
class named 'OldPrinterAdapter' that implements the 'Printer' interface and uses an instance of the 'OldPrinter' class to print
messages. The 'ModernPrinter' class uses an instance of the 'OldPrinterAdapter' class to print messages. This way, the 'ModernPrinter'
class can use the 'OldPrinter' class to print messages without any changes to the 'OldPrinter' class.

