from Account import Account


class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def withdrawal(self, amount):
        if amount < 2000:
            super().withdrawal(amount)
        else:
            print("You cannot withdraw above your limit", self.interestrate)


savings = SavingsAccount()
savings.withdrawal(2000)