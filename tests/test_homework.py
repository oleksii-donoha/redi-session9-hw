# def test_nothing():
#     assert True

import unittest
import pytest
from random import uniform
from src.homework import cool_piecewise_function

def test_py_6():
    x = uniform(-100, -6.001)
    assert cool_piecewise_function(x) == 25

def test_py_6_5():
    x = uniform(-6, -5)
    assert cool_piecewise_function(x) == None

def test_py_5_2():
    x = uniform(-4.999, 2)
    assert cool_piecewise_function(x) == (x ** 2)

def test_py_2():
    x = uniform(2, 100)
    assert cool_piecewise_function(x) == (-5 * (x - 2) + 4)

class DmytroTestCase(unittest.TestCase):

    def test_unit_6(self):
        x = uniform(-100, -6.001)
        y = cool_piecewise_function(x)
        # y = cool_piecewise_function(-6.001)
        self.assertEqual(y, 25)

    def test_unit_6_5(self):
        x = uniform(-6, -5)
        y = cool_piecewise_function(x)
        self.assertEqual(y, None)
    def test_unit_5_2(self):
        x = uniform(-4.999, 2)
        y = cool_piecewise_function(x)
        self.assertEqual(y, (x ** 2))

    def test_unit_2(self):
        x = uniform(2, 100)
        y = cool_piecewise_function(x)
        self.assertEqual(y, (-5 * (x - 2) + 4))

if __name__ == '__main__':
    unittest.main()
