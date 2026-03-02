"""
Jalen Banks
Lab 9, Unit Testing - BankAccount
Mar 1, 2026
"""

import unittest

from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Jalen", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit_adds_to_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw_subtracts_from_balance(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    def test_withdraw_more_than_balance_raises_exception(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_sequence_of_deposits_and_withdrawals(self):
        self.account.deposit(25)
        self.account.withdraw(10)
        self.account.deposit(35)
        self.account.withdraw(20)
        self.assertEqual(self.account.get_balance(), 130)


if __name__ == '__main__':
    unittest.main()
