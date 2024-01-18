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

        # Deposit a positive amount
        deposit_amount = 100
        AccountService.deposit(account.account_id, deposit_amount)
        updated_balance = account.get_balance()

        self.assertEqual(updated_balance, initial_balance + deposit_amount)

        # Deposit a zero amount
        AccountService.deposit(account.account_id, 0)
        self.assertEqual(account.get_balance(), updated_balance)

        # Attempt to deposit a negative amount
        with self.assertRaises(ValueError):
            AccountService.deposit(account.account_id, -50)

    def test_withdraw(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")
        initial_balance = account.get_balance()

        # Deposit an amount for testing withdrawal
        deposit_amount = 200
        AccountService.deposit(account.account_id, deposit_amount)

        # Withdraw a positive amount
        withdraw_amount = 50
        AccountService.withdraw(account.account_id, withdraw_amount)
        updated_balance = account.get_balance()

        self.assertEqual(updated_balance, initial_balance + deposit_amount - withdraw_amount)

        # Attempt to withdraw a zero amount
        AccountService.withdraw(account.account_id, 0)
        self.assertEqual(account.get_balance(), updated_balance)

        # Attempt to withdraw more than the current balance
        with self.assertRaises(ValueError):
            AccountService.withdraw(account.account_id, updated_balance + 1)

        # Attempt to withdraw a negative amount
        with self.assertRaises(ValueError):
            AccountService.withdraw(account.account_id, -20)

    def test_withdraw_more_than_balance(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")

        # Attempt to withdraw more than the current balance
        withdraw_amount = 50
        with self.assertRaises(ValueError):
            AccountService.withdraw(account.account_id, withdraw_amount)

    def test_deposit_negative_value(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")

        # Attempt to deposit a negative amount
        deposit_amount = -50
        with self.assertRaises(ValueError):
            AccountService.deposit(account.account_id, deposit_amount)

    def test_transaction_rollback_on_error(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")

        # Deposit an amount
        deposit_amount = 100
        AccountService.deposit(account.account_id, deposit_amount)

        # Attempt to deposit a negative amount (should trigger a ValueError and rollback the transaction)
        with self.assertRaises(ValueError):
            AccountService.deposit(account.account_id, -50)

        # Verify that the balance remains unchanged
        self.assertEqual(account.get_balance(), deposit_amount)

    def test_multiple_transactions(self):
        account = AccountService.create_account(customer_id="123", name="John Doe")

        # Deposit an amount
        deposit_amount_1 = 100
        AccountService.deposit(account.account_id, deposit_amount_1)

        # Start a new transaction and deposit another amount
        with AccountService.Transaction():
            deposit_amount_2 = 50
            AccountService.deposit(account.account_id, deposit_amount_2)

            # Verify that the balance is the sum of both deposits within this transaction
            self.assertEqual(account.get_balance(), deposit_amount_1 + deposit_amount_2)

        # Verify that the balance is the same after the transaction
        self.assertEqual(account.get_balance(), deposit_amount_1 + deposit_amount_2)
