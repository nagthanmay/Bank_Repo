import unittest
from Service.account_service import AccountService
from Domain.account import Account

class TestAccountService(unittest.TestCase):
    def test_create_account(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")
        self.assertIsNotNone(account)

    def test_deposit(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")
        initial_balance = account.get_balance()

        # Deposit an amount
        deposit_amount = 100
        AccountService.deposit(account.account_id, deposit_amount)
        updated_balance = account.get_balance()

        self.assertEqual(updated_balance, initial_balance + deposit_amount)

    def test_withdraw(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")
        initial_balance = account.get_balance()

        # Deposit an amount for testing withdrawal
        deposit_amount = 200
        AccountService.deposit(account.account_id, deposit_amount)

        # Withdraw an amount
        withdraw_amount = 50
        AccountService.withdraw(account.account_id, withdraw_amount)
        updated_balance = account.get_balance()

        self.assertEqual(updated_balance, initial_balance + deposit_amount - withdraw_amount)

    def test_deposit_negative_value(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")
        
        # Attempt to deposit a negative amount
        deposit_amount = -50
        with self.assertRaises(ValueError):
            AccountService.deposit(account.account_id, deposit_amount)

    def test_withdraw_negative_value(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")
        
        # Attempt to withdraw a negative amount
        withdraw_amount = -20
        with self.assertRaises(ValueError):
            AccountService.withdraw(account.account_id, withdraw_amount)

    def test_withdraw_more_than_balance(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")
        
        # Attempt to withdraw more than the current balance
        withdraw_amount = 50
        with self.assertRaises(ValueError):
            AccountService.withdraw(account.account_id, withdraw_amount)
