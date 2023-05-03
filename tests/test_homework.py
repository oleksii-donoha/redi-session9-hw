from src.homework import cool_piecewise_function

def test_none():
    """ for y = 25
        """
    assert cool_piecewise_function(-6) == None

def test_none2():
    """ for y = 25
        """
    assert cool_piecewise_function(-5.5) == None


def test_zero():
    """   for y =  x**2
        """
    assert cool_piecewise_function(0) == 0


def test_start():
    """ for y = -5 * (x - 2) + 4
       """
    assert cool_piecewise_function(2) == 4


# def test_axisCross():
#     """ for y = -5 * (x - 2) + 4 перевірка не пройдена
#             """
#     assert cool_piecewise_function(2.8) == 0
#