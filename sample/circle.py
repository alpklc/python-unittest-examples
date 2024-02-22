"""
https://www.pythontutorial.net/python-unit-testing/
"""

import math
from .shape import Shape

class Circle(Shape):
    def __init__(self, radius : int | float) -> None:
        if type(radius) not in (int, float):
            raise TypeError('Radius must be an integer of float')
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        
        self._radius = radius
    

    def area(self) -> int | float:
        return math.pi * math.pow(self._radius, 2)