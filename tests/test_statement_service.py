import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from Service.statement_service import StatementService
from Domain.account import Account
from Infra.account_repository import AccountRepository


class TestStatementService(unittest.TestCase):
    def setUp(self):
        # Set up a test account
        self.test_account = Account(account_id="1", customer_id="123", account_number="ACC123", balance=100)
        AccountRepository.save_account(self.test_account)

    def test_generate_account_statement_positive(self):
        statement = StatementService.generate_account_statement(account_id=self.test_account.account_id)
        # Implement assertion for the generated statement
        self.assertIsNotNone(statement)

    def test_generate_account_statement_negative(self):
        # Test with an invalid account ID
        with self.assertRaises(ValueError):
            StatementService.generate_account_statement(account_id="invalid_account_id")
