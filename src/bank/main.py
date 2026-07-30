from bank.bank_account import BankAccount
from bank.gold_account import GoldAccount

regular = BankAccount("A100", "John Smith", 50)
gold = GoldAccount("G200", "Mary Jones", 50)

regular.withdraw_funds(70)
gold.withdraw_funds(70)

print("Regular Account:")
regular.print_info()

print("\nGold Account:")
gold.print_info()
