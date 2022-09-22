import unittest

from account.exception import AccountWithdrawalException
from .account import Account


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.acc = Account("Elder Jega")

    def test_account_can_be_created(self):
        # acc = Account()
        self.assertIsNotNone(self.acc)

    def test_that_account_has_zero_balance_on_creation(self):
        # acc = Account()
        self.assertEqual(0, self.acc.balance)

    def test_that_account_has_a_name(self):
        # acc = Account("Elder Jega")
        self.assertEqual("Elder Jega", self.acc.name)

    def test_that_account_can_be_deposited_into(self):
        self.acc.deposit(1500)
        self.assertEqual(1500, self.acc.balance)

    def test_that_account_can_be_withdrawn_from(self):
        self.acc.deposit(1500)
        self.acc.withdrawal(250)
        self.assertEqual(1250, self.acc.balance)

    def test_that_account_cannot_be_over_withdrawn_from(self):
        self.acc.deposit(1500)
        with self.assertRaises(AccountWithdrawalException):
            self.acc.withdrawal(2500)
            
        # def test_that_money_can_be_transferred_between_two_accounts(self):


if __name__ == '__main__':
    unittest.main()
