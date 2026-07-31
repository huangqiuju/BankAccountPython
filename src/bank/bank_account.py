class BankAccount:
    def __init__(
        self: "BankAccount", account_id: int, full_name: str, initial_balance: float
    ) -> None:
        self._account_id = account_id
        self._full_name = full_name
        self._balance = initial_balance

    def add_funds(self: "BankAccount", amount: float) -> None:
        self._balance += amount

    def withdraw_funds(self: "BankAccount", amount: float) -> None:
        self._balance -= amount

        if self._balance < 0:
            self._balance -= 20  # overdraft penalty

    def print_info(self: "BankAccount") -> None:
        print(f"Account ID: {self._account_id}")
        print(f"Full Name: {self._full_name}")
        print(f"Balance: ${self._balance}")
