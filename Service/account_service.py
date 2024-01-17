import os
import sys
# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Domain.account import Account
from Infra.account_repository import AccountRepository
from Domain.customer import Customer
import uuid

def generate_unique_id():
    # Generate a new UUID (Universally Unique Identifier)
    unique_id = str(uuid.uuid4())

    return unique_id

def generate_account_number():
        return str(uuid.uuid4().hex)[:10]  # Use the first 10 characters of the UUID as the account number


class AccountService:
    @staticmethod
    def create_account(customer_id, name, email=None, phone_number=None):
        try:
            account_id = generate_unique_id()  
            account_number = generate_account_number()

            account = Account(account_id, customer_id, account_number, balance=0)
            customer = Customer(customer_id=customer_id, name=name, email=email, phone_number=phone_number)
            AccountRepository.save_account(account)

            return account

        except Exception as e:
            print(f"Error creating account: {e}")
            raise e

    @staticmethod
    def deposit(account_id, amount):
        try:
            account = AccountRepository.find_account_by_id(account_id)

            if not account:
                raise ValueError("Account not found.")

            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")

            account.deposit(amount)
            AccountRepository.save_account(account)

        except Exception as e:
            print(f"Error depositing amount: {e}")
            raise e

    @staticmethod
    def withdraw(account_id, amount):
        try:
            account = AccountRepository.find_account_by_id(account_id)

            if not account:
                raise ValueError("Account not found.")

            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")

            if amount > account.get_balance():
                raise ValueError("Insufficient funds for withdrawal.")

            account.withdraw(amount)
            AccountRepository.save_account(account)

        except Exception as e:
            print(f"Error withdrawing amount: {e}")
            raise e
