import threading

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

    @classmethod
    def nested_transaction(cls):
        return NestedTransactionManager()

class NestedTransactionManager:
    def __enter__(self):
        TransactionManager._local_data.transaction_depth += 1
        print("Nested transaction started.")

    def __exit__(self, exc_type, exc_value, traceback):
        TransactionManager._local_data.transaction_depth -= 1

        if TransactionManager._local_data.transaction_depth == 0:
            if exc_type is None:
                # Commit the transaction if no exception occurred
                print("Nested transaction committed.")
            else:
                # Rollback the transaction if an exception occurred
                print("Nested transaction rolled back.")
