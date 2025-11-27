# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.


class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.acc_no = acc
        print(f"new account {acc} created | Initial balance: {self.balance}")

    # debit
    def debit(self, amount):
        self.balance -= amount
        print(f"Debited: {amount} and Current balance: {self.get_balance()}")

    # credit
    def credit(self, amount):
        self.balance += amount
        print(f"Credited: {amount} and current ballance: {self.get_balance()}")

    # get ballance
    def get_balance(self):
        return self.balance


account1 = Account(12000, 714384)
account1.credit(3000)
account1.debit(5000)
