import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Domain.account import Account
from Infra.account_repository import AccountRepository


class TransactionService:
    @staticmethod
    def make_transaction(account_id, amount, transaction_type):
        account = AccountRepository.find_account_by_id(account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")
