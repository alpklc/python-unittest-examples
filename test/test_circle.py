"""
https://www.pythontutorial.net/python-unit-testing/
"""

import unittest
import math

from sample.circle import Circle
from sample.shape import Shape

class TestCircle(unittest.TestCase):
    def test_circle_instance_of_shape(self) -> None:
        circle = Circle(10)
        self.assertIsInstance(circle, Shape)
    

    def test_circle_negative_radius(self) -> None:
        with self.assertRaises(ValueError):
            circle = Circle(-1)
    

    def test_circle_radius_type(self) -> None:
        with self.assertRaises(TypeError):
            circle = Circle('5')


    def test_circle_area(self) -> None:
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.area(), math.pi * 2.5 * 2.5)


if __name__ == '__main__':
    unittest.main()

