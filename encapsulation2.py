class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def _show_balance(self):
        return self.balance

    def __update_balance(self, amount):
        self.balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            print(self._show_balance())
        else:
            print("Invalid deposit amount!")


account = BankAccount(1000)
account._show_balance()     # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)
