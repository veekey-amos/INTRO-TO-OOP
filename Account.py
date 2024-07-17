class Account:
    def __init__(self):
        self.balance =10000
        print("starting balance is: ", self.balance)

    def deposit(self, amount):
        self.balance = amount + self.balance
        print("new balance is: ", self.balance)

    def withdrawal(self, amount):
        self.balance = self.balance - amount

account = Account()
account.deposit(2000)
