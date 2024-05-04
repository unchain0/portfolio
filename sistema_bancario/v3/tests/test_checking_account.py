import unittest
from datetime import date

from sistema_bancario.v3.models.checking_account import CheckingAccount
from sistema_bancario.v3.models.customer import Customer


class TestCheckingAccount(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", "Doe", date(2000, 1, 1), "New York")
        self.checking_account = CheckingAccount(1, self.customer)
        self.checking_account.deposit(500)

    def test_init(self):
        self.assertEqual(self.checking_account.number, 1)
        self.assertEqual(self.checking_account.customer, self.customer)
        self.assertEqual(self.checking_account.limit, 500)
        self.assertEqual(self.checking_account.limit_withdrawals, 3)

    def test_number_of_withdrawals_limit(self):
        self.assertEqual(self.checking_account.limit_withdrawals, 3)

    def test_withdrawal_within_limit(self):
        result = self.checking_account.withdraw(100)
        self.assertTrue(result)

    def test_withdrawal_beyond_limit(self):
        result = self.checking_account.withdraw(1000)
        self.assertFalse(result)

    def test_too_many_withdrawals(self):
        for _ in range(3):
            self.checking_account.withdraw(20)
        result = self.checking_account.withdraw(100)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
