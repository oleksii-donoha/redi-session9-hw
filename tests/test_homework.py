import unittest
from src.homework import cool_piecewise_function

#def test_nothing():
    #assert True

def test_25():
    assert cool_piecewise_function(-7) == 25
    assert cool_piecewise_function(-10) == 25

def test_parabola():
    assert cool_piecewise_function(-4) == 16
    assert cool_piecewise_function(0) == 0
    assert cool_piecewise_function(1) == 1

def test_line():
    assert cool_piecewise_function(2) == 4
    assert cool_piecewise_function(3) == -1
    assert cool_piecewise_function(10) == -36

def test_None():
    assert cool_piecewise_function(-5) == None
    assert cool_piecewise_function(-6) == None
    assert cool_piecewise_function(-5.5) == None

class Mytestcase(unittest.TestCase):

    def test25(self):
        result = cool_piecewise_function(-10)
        self.assertEqual(result,25)
        result =cool_piecewise_function(-7)
        self.assertEqual(result,25)

    def testParabola(self):
        result = cool_piecewise_function(0)
        self.assertEqual(result,0)

    def testLine(self):
        result = cool_piecewise_function(2)
        self.assertEqual(result,4)

    def testNone(self):
        result = cool_piecewise_function(-5)
        self.assertEqual(result,None)

