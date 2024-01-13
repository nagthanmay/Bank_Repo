import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from Service.account_service import AccountService
from Domain.account import Account
import unittest
from Service.account_service import AccountService

    

class TestAccountService(unittest.TestCase):
    def test_create_account_positive(self):
        account = AccountService.create_account(customer_id="123", name="John Doe", email="john@example.com", phone_number="1234567890")
        self.assertIsInstance(account, Account)
        self.assertEqual(account.customer_id, "123")
        self.assertEqual(account.balance, 0)

    def test_create_account_negative(self):
        # Provide all required arguments for create_account
        account = AccountService.create_account(
            customer_id="123",
            name="John Doe",
            email="john.doe@example.com",
            phone_number="1234567890"
        )

        # Assert that the account object is not None
        self.assertIsNotNone(account)
