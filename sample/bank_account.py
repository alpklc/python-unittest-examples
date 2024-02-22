"""
https://www.pythontutorial.net/python-unit-testing/
"""

class InsufficientFund(Exception):
    pass


class BankAccount:
    def __init__(self, balance : int | float) -> None:
        if type(balance) not in (int, float):
            raise TypeError('Balance must be an integer of float')
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = balance
    

    @property
    def balance(self) -> int | float:
        return self._balance
    

    def deposit(self, amount : int | float) -> None:
        if type(amount) not in (int, float):
            raise TypeError('Balance must be an integer of float')
        if amount <= 0:
            raise ValueError('The amount must be positive')
        self._balance += amount
    

    def withdraw(self, amount : int | float) -> None:
        if type(amount) not in (int, float):
            raise TypeError('Balance must be an integer of float')
        if amount <= 0:
            raise ValueError('The withdrawal amount must be more than 0')  
        if amount > self._balance:
            raise InsufficientFund('Insufficient amount for withdrawal')
        self._balance -= amount
    

