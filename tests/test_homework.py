from src.homework import cool_piecewise_function

def test_none():
    assert cool_piecewise_function(-6) == None

def test_none2():
    assert cool_piecewise_function(-5.5) == None
    """ for y = 25
    """

def test_zero():
    assert cool_piecewise_function(0) == 0
    """   for y =  x**2
    """

def test_start():
    assert cool_piecewise_function(2) == 4
    """ for y = -5 * (x - 2) + 4
    """

def test_axisCross():
    assert cool_piecewise_function(2.8) == 0
    """ for y = -5 * (x - 2) + 4 перевірка не пройдена
        """