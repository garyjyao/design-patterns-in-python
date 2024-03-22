from unittest.mock import patch
from design_patterns.structural.bridge_pattern.bridge_pattern import BankAccount, FileLogger, ConsoleLogger


class TestBridgePattern:
    @patch.object(FileLogger, 'log')
    @patch.object(ConsoleLogger, 'log')
    def test_bank_account_with_file_logger(self, mock_console_log, mock_file_log):
        # Assign
        bank_account = BankAccount()
        bank_account.set_logger(FileLogger())

        # Act
        bank_account.deposit(100)

        # Assert
        mock_file_log.assert_called_with("deposit 100")
        mock_console_log.assert_not_called()

    @patch.object(FileLogger, 'log')
    @patch.object(ConsoleLogger, 'log')
    def test_bank_account_with_console_logger(self, mock_console_log, mock_file_log):
        # Assign
        bank_account = BankAccount()
        bank_account.set_logger(ConsoleLogger())

        # Act
        bank_account.withdraw(100)

        # Assert
        mock_console_log.assert_called_with("withdraw 100")
        mock_file_log.assert_not_called()
