from Account import Account


class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

currentAccount = CurrentAccount()
currentAccount.deposit(5000)
currentAccount.withdrawal(3000)