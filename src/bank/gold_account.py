from bank.bank_account import BankAccount


class GoldAccount(BankAccount):
    def withdraw_funds(self, amount):
        self.balance -= amount  # no overdraft penalty
