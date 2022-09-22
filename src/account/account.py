from account.exception import AccountWithdrawalException


class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, deposit_amount):
        # self.deposit_amount = deposit_amount
        self.balance += deposit_amount

    def withdrawal(self, withdraw_amount):
        # self.withdraw_amount = withdraw_amount
        if withdraw_amount > self.balance:
            balance = self.balance
            raise AccountWithdrawalException("Your withdrawal is invalid. Withdrawal is higher than your balance")
        else:
            self.balance -= withdraw_amount
