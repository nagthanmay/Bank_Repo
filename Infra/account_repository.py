import threading

class AccountRepository:
    accounts = {}

    @staticmethod
    def save_account(account):
        AccountRepository.accounts[account.account_id] = account

    @staticmethod
    def find_account_by_id(account_id):
        return AccountRepository.accounts.get(account_id)

    @staticmethod
    def find_accounts_by_customer_id(customer_id):
        return [account for account in AccountRepository.accounts.values() if account.customer_id == customer_id]



class TransactionManager:
    _local_data = threading.local()

    @classmethod
    def __enter__(cls):
        cls._local_data.transaction_depth = getattr(cls._local_data, 'transaction_depth', 0) + 1

        if cls._local_data.transaction_depth == 1:
            # Start the transaction or any initialization logic here
            print("Transaction started.")

        return cls

    @classmethod
    def __exit__(cls, exc_type, exc_value, traceback):
        cls._local_data.transaction_depth -= 1

        if cls._local_data.transaction_depth == 0:
            if exc_type is None:
                # Commit the transaction if no exception occurred
                print("Transaction committed.")
            else:
                # Rollback the transaction if an exception occurred
                print("Transaction rolled back.")

    @classmethod
    def is_in_transaction(cls):
        return getattr(cls._local_data, 'transaction_depth', 0) > 0

