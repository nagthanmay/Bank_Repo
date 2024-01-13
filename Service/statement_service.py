import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Domain.account import Account
from Infra.account_repository import AccountRepository


class StatementService:
    @staticmethod
    def generate_account_statement(account_id):
        account = AccountRepository.find_account_by_id(account_id)

        if not account:
            raise ValueError("Account not found")

        transactions = StatementService.get_transactions(account_id)
        statement = f"Account Statement for Account {account.account_number}:\n"

        for transaction in transactions:
            statement += f"{transaction['date']} - {transaction['type']} - Amount: {transaction['amount']}\n"

        statement += f"Current Balance: {account.get_balance()}"

        return statement

    @staticmethod
    def get_transactions(account_id):
        # Placeholder method, replace with actual logic to retrieve transactions from a data source
        # For example, you could have a TransactionRepository for storing and retrieving transactions.
        # This method might return a list of dictionaries with transaction details.
        # Example: [{'date': '2024-01-15', 'type': 'Deposit', 'amount': 50}, ...]
        return [{'date': '2024-01-15', 'type': 'Deposit', 'amount': 50}, {'date': '2024-01-16', 'type': 'Withdraw', 'amount': 20}]
