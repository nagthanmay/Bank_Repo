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
