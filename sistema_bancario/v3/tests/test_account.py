import unittest
from datetime import date

from sistema_bancario.v3.models.account import Account
from sistema_bancario.v3.models.customer import Customer


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(name='Felippe', cpf='123.456.789-10', birth_date=date(2000, 1, 1), address='New York')
        self.account = Account.new_account(self.customer, 1)

    def test_new_account(self):
        self.assertIsInstance(self.account, Account)

    def test_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_bank_number(self):
        self.assertEqual(self.account.number, 1)

    def test_agency(self):
        self.assertEqual(self.account.agency, '0001')

    def test_customer(self):
        self.assertEqual(self.account.customer, self.customer)

    def test_withdraw_less_than_twenty(self):
        self.assertFalse(self.account.withdraw(10))

    def test_insufficient_balance(self):
        self.assertFalse(self.account.withdraw(100))

    def test_successful_withdrawal(self):
        self.account.deposit(100)
        self.assertTrue(self.account.withdraw(25))

    def test_deposit_less_than_twenty_five(self):
        self.assertFalse(self.account.deposit(20))

    def test_successful_deposit(self):
        self.assertTrue(self.account.deposit(50))


if __name__ == '__main__':
    unittest.main()
