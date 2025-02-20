import random
from Dsa_Function.azBank.account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def _generate_account_number(self):
        while True:
            account_number = str(random.randint(1000000000, 9999999999))
            if account_number not in self.accounts:
                return account_number

    def create_account(self, first_name, last_name, pin, initial_deposit=0):
        account_number = self._generate_account_number()
        account = Account(account_number, first_name, last_name, pin, initial_deposit)
        self.accounts[account_number] = account
        return account

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number].withdraw(amount)

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number].get_balance()

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            raise ValueError("One or both account numbers not found.")
        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)
        return True

    def close_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        del self.accounts[account_number]
        return True
