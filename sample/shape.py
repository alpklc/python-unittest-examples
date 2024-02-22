"""
https://www.pythontutorial.net/python-unit-testing/
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area() -> int | float:
        pass