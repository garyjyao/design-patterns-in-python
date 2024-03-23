from unittest.mock import patch
from design_patterns.structural.adapter_object_pattern.old_new_printer import OldPrinter, PrinterAdapter, ModernPrinter


class TestAdapterPattern:
    @patch.object(OldPrinter, 'print_old')
    def test_old_printer_adapter(self, mock_print_old):
        # Assign
        old_printer_adapter = PrinterAdapter(OldPrinter())

        # Act
        old_printer_adapter.print("Hello, Adapter Pattern with Old Printer!")

        # Assert
        mock_print_old.assert_called_with("Hello, Adapter Pattern with Old Printer!")


class TestModernPrinter:
    @patch.object(ModernPrinter, 'print')
    def test_modern_printer(self, mock_print):
        # Assign
        modern_printer = ModernPrinter()

        # Act
        modern_printer.print("Hello, from Modern Printer!")

        # Assert
        mock_print.assert_called_with("Hello, from Modern Printer!")


class TestOldPrinter:
    @patch.object(OldPrinter, 'print_old')
    def test_old_printer(self, mock_print_old):
        # Assign
        old_printer = OldPrinter()

        # Act
        old_printer.print_old("Hello, from Old Printer!")

        # Assert
        mock_print_old.assert_called_with("Hello, from Old Printer!")
