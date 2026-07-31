from bank.bank_account import BankAccount


class GoldAccount(BankAccount):
    def withdraw_funds(self: "GoldAccount", amount: float):
        self._balance -= amount  # no overdraft penalty
