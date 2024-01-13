import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Domain.account import Account
from Infra.account_repository import AccountRepository
from Domain.customer import Customer
import random
import string
import uuid

def generate_unique_id():
    # Generate a new UUID (Universally Unique Identifier)
    unique_id = str(uuid.uuid4())

    return unique_id

def generate_account_number():
    # Choose a prefix for the account number (e.g., "ACC" for Account)
    prefix = "ACC"

    # Generate a random 6-digit number
    random_number = ''.join(random.choices(string.digits, k=6))

    # Concatenate the prefix and random number to form the account number
    account_number = f"{prefix}{random_number}"

    return account_number

class AccountService:
    @staticmethod
    def create_account(customer_id, name, email, phone_number):
        account_number = generate_account_number()  # You can implement this method
        account = Account(account_id=generate_unique_id(), customer_id=customer_id, account_number=account_number)
        customer = Customer(customer_id=customer_id, name=name, email=email, phone_number=phone_number)
        return account
