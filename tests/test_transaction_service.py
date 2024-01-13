import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from Service.transaction_service import TransactionService
from Domain.account import Account
from Infra.account_repository import AccountRepository


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        # Set up a test account
        self.test_account = Account(account_id="1", customer_id="123", account_number="ACC123", balance=100)
        AccountRepository.save_account(self.test_account)

    def test_make_deposit_positive(self):
        TransactionService.make_transaction(account_id=self.test_account.account_id, amount=50, transaction_type='deposit')
        self.assertEqual(self.test_account.balance, 150)

    def test_make_withdrawal_negative(self):
        # Test withdrawal with insufficient balance
        with self.assertRaises(ValueError):
            TransactionService.make_transaction(account_id=self.test_account.account_id, amount=200, transaction_type='withdraw')
