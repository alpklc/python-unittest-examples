"""
https://www.pythontutorial.net/python-unit-testing/
"""

import math
from .shape import Shape

class Square(Shape):
    def __init__(self, length : int | float) -> None:
        if type(length) not in (int, float):
            raise TypeError('Length must be an integer or float')
        if length < 0:
            raise ValueError('Length cannot be negative')
        
        self._length = length


    def area(self) -> int | float:
        return math.pow(self._length, 2)