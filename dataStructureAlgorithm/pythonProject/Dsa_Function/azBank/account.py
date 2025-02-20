class Account:
    def __init__(self, account_number, first_name, last_name, pin, initial_deposit=0):
        pin = str(pin)
        if not (pin.isdigit() and len(pin) == 4):
            raise ValueError("PIN must be exactly 4 digits.")
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
