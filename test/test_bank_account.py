"""
https://www.pythontutorial.net/python-unit-testing/
"""

import unittest

from sample.bank_account import BankAccount
from sample.bank_account import InsufficientFund

def setUpModule() -> None:
    """
    Module-level fixture
    """
    # print('Running setUpModule - (Module-level fixture)')


def tearDownModule() -> None:
    """
    Module-level fixture
    """
    # print('Running tearDownModule - (Module-level fixture)')


class TestBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        Class-level fixture
        """
        # print('Running setUpClass - (Class-level fixture)')


    @classmethod
    def tearDownClass(cls) -> None:
        """
        Class-level fixture
        """
        # print('Running tearDownClass - (Class-level fixture)')


    def setUp(self) -> None:
        """
        Method-level fixture
        """
        # print('Running setUp - (Method-level fixture)')
        self.bank_account = BankAccount(100)


    def tearDown(self) -> None:
        """
        Method-level fixture
        """
        # print('Running tearDown - (Method-level fixture)')
        self.bank_account = None
    
    
    def test_deposit(self) -> None:
        self.bank_account.deposit(100)
        self.assertEqual(self.bank_account.balance, 200)
    

    def test_withdraw(self) -> None:
        self.bank_account.withdraw(50)
        self.assertEqual(self.bank_account.balance, 50)
    

    def test_bank_account_balance_value(self) -> None:
        with self.assertRaises(ValueError):
            BankAccount(-10)
    

    def test_deposit_amount_type(self) -> None:
        with self.assertRaises(TypeError):
            BankAccount('100').deposit(10)


    def test_deposit_negative_or_zero_amount(self) -> None:
        with self.assertRaises(ValueError):
            BankAccount(20).deposit(-10)


    def test_withdraw_amount_type(self) -> None:
        with self.assertRaises(TypeError):
            BankAccount('100').withdraw(10)
    

    def test_withdraw_negative_or_zero_amount(self) -> None:
        with self.assertRaises(ValueError):
            BankAccount(20).withdraw(-10)
    

    def test_enough_money_to_withdraw(self) -> None:
        with self.assertRaises(InsufficientFund):
            BankAccount(20).withdraw(30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
