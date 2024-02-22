"""
https://www.pythontutorial.net/python-unit-testing/
"""

import unittest

from sample.square import Square
from sample.shape import Shape

class TestSquare(unittest.TestCase):
    def test_square_negative_length(self) -> None:
        with self.assertRaises(ValueError):
            square = Square(-1)
    

    def test_square_length_type(self) -> None:
        with self.assertRaises(TypeError):
            square = Square('5')


    def test_square_instance_of_shape(self) -> None:
        square = Square(5)
        self.assertIsInstance(square, Shape)


    def test_square_area(self) -> None:
        square = Square(10)
        self.assertEqual(square.area(), 100)
    

if __name__ == '__main__':
    unittest.main()


