import io
import unittest


# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
# doctest,
# unittest,
# pytest

# doctest

def is_natural(a: int) -> bool:
    """
Проверка числа А на натуральность , оно должно делиться на 2 и на само себя  [2, A).
    >>> is_natural(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
        ...
    TypeError: Число А должно быть int
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: Число А должно быть больше 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: Число А должно быть больше 1


    """
    if not isinstance(а, int):
        raise TypeError('Число А должно быть int')
    elif а < 2:
        raise ValueError('Число А должно быть больше 1')
    for i in range(2, а):
         if a % i == 0:
            return False
    return True


class Test_Natural:

     def test_is_prime(self):
        self.assertFalse(is_natural(42))
        self.assertTrue(is_natural(73))

    def test_type(self):
        self.assertRaises(TypeError, is_natural, 3.14)
    
    def test_value(self):
        with self.assertRaises(ValueError):
            is_natural(-100)
            is_natural(1)
    
    


def test_is_natural():
    assert not is_natural(42), '42 - составное число'
    assert is_natural(73), '73 - простое число'
def test_type():
    with pytest.raises(TypeError):
        is_natural(3.14)
def test_value():
    with pytest.raises(ValueError):
        is_natural(-100)
def test_value_with_text():
    with pytest.raises(ValueError, match=r'Число А должно быть больше 1 '):
is_natural(1)
