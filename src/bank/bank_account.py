class BankAccount:
    def __init__(self, account_id, full_name, initial_balance):
        self.account_id = account_id
        self.full_name = full_name
        self.balance = initial_balance

    def add_funds(self, amount):
        self.balance += amount

    def withdraw_funds(self, amount):
        self.balance -= amount

        if self.balance < 0:
            self.balance -= 20  # overdraft penalty

    def print_info(self):
        print(f"Account ID: {self.account_id}")
        print(f"Full Name: {self.full_name}")
        print(f"Balance: ${self.balance}")
