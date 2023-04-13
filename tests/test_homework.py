# def test_nothing():
#     assert True

import unittest
from random import uniform

from src.homework import cool_piecewise_function

class DmytroTestCase(unittest.TestCase):

    def test_6(self):
        x = uniform(-100, -6.001)
        y = cool_piecewise_function(x)
        # y = cool_piecewise_function(-6.001)
        self.assertEqual(y, 25)

    def test_6_5(self):
        x = uniform(-6, -5)
        y = cool_piecewise_function(x)
        self.assertEqual(y, None)
    def test_5_2(self):
        x = uniform(-4.999, 2)
        y = cool_piecewise_function(x)
        self.assertEqual(y, (x ** 2))

    def test_2(self):
        x = uniform(2, 100)
        y = cool_piecewise_function(x)
        self.assertEqual(y, (-5 * (x - 2) + 4))

if __name__ == '__main__':
    unittest.main()
