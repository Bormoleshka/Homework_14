import unittest
import pytest


def get_number(num: int, mod: int = 10) -> str:
    """
    Функция получает на вход целое число, систему исчисления и возвращает его  строковое представление.
    : number: само число
    : mod: система исчисления
    : return: строковое представление
    >>> get_number(57, 2)
    '111001'
    >>> get_number(57, 3)
    '2010'
    >>> get_number(57, 4)
    '321'
    >>> get_number(57, 5)
    '212'
    >>> get_number(57, 6)
    '133'
    
    """
    result = ''
    while num != 0:
        result = str(num % mod) + result
        num //= mod
    return result
    
    
    
print(get_number(57, 2))
print(get_number(57, 3))
print(get_number(57, 4))
print(get_number(57, 5))
print(get_number(57, 6))


class TestCaseNumbers(unittest.TestCase):
    def test_unit_2(self):
        self.assertEqual(get_number(57, 2), '111001', msg='Test failed')

    def test_unit_3(self):
        self.assertEqual(get_number(57, 3), '2010', msg='Test failed')

    def test_unit_4(self):
        self.assertEqual(get_number(57, 4), '321', msg='Test failed')

    def test_unit_5(self):
        self.assertEqual(get_number(57, 5), '212', msg='Test failed')
        
    def test_unit_6(self):
        self.assertEqual(get_number(57, 5), '133', msg='Test failed')
        
        
        
def test_py_2():
    assert get_number(57, 2) == '111001', 'Test failed'


def test_py_3():
    assert get_number(57, 3) == '2010', 'Test failed'


def test_py_4():
    assert get_number(57, 4) == '321', 'Test failed'


def test_py_5():
    assert get_number(57, 5) == '212', 'Test failed'


def test_py_6():
    assert get_number(57, 6) == '133', 'Test failed'
    
    
if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    unittest.main()
    pytest.main()
