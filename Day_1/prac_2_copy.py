class Account:
    def __init__(self, acc_no, balance):
        print(f"new user {acc_no} created | initial balance {balance}")
        self.acc_no = acc_no
        self.balance = balance

    # credit
    def credit(self, ammount):
        self.balance += ammount
        print(f"{ammount} BDT credited | and Total balance: {self.get_balance()}")

    # debit
    def debit(self, ammount):
        self.balance -= ammount
        print(f"{ammount} BDT credited | and Total balance: {self.get_balance()}")

    # get total balance
    def get_balance(self):
        return self.balance


acc1 = Account(341190, 60000)
acc2 = Account(341191, 13000)
acc3 = Account(341192, 5000)

acc2.credit(1000)
acc1.credit(4000)
acc3.credit(8000)

acc2.debit(10000)
acc2.debit(30000)
acc2.debit(12000)
