import logging
import collections
from typing import DefaultDict, Dict
import json
import csv


logging.basicConfig(filename='log.log', level=logging.NOTSET, encoding='utf-8')

logging.basicConfig(filename='error.log',
                    level=logging.ERROR, encoding='utf-8')


class Rectangle:
    '''Класс подсчета площади и периметра прямоугольника'''
    __slots__ = ('side_1', 'side_2')

    def __init__(self, side_1, side_2=None):
        '''Иницилизация сторон прямоугольника'''
        self.side_1 = side_1
        self.side_2 = side_2 if side_2 is not None else side_1

    @property
    def side_1(self):
        return self.side_1

    @property
    def side_2(self):
        return self.side_2

    @side_1.setter
    def side_1(self, value):
        if value > 0:
            self.side_1 = value
        else:
            raise ValueError('Введите положительное число')

    @side_2.setter
    def side_2(self, value):
        if value > 0:
            self.side_2 = value
        else:
            raise ValueError('Введите положительное число')

    def area(self):
        '''Подсчет площади прямоугольника'''
        return self.side_2 * self.side_1
    logging.basicConfig(level=logging.NOTSET)

    def perimetr(self):
        '''Подсчет периметра прямоугольника'''
        return 2 * (self.side_1 + self.side_2)
    logging.info('Подсчет периметра прямоугольника')

    def __add__(self, other):
        '''Подсчет стороны прямоугольника из его площади '''
        new_perimetr = self.perimetr() + other.perimetr()
        new_a = self.side_1
        new_b = new_perimetr / 2 - new_a
        return Rectangle(new_a, new_b)
    # print(__add__.__doc__)

    def __sub__(self, other):
        new_perimetr = abs(self.perimetr() + other.perimetr())
        new_a = min([self.side_1, self.side_2, other.side1, other.side2])
        new_b = new_perimetr / 2 - new_a
        return Rectangle(new_a, new_b)
    # print(__sub__.__doc__)


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
        logging.ERROR(f'Ошибка типа данных , ввели число с плавующей точкой {test_is_natural}')
def test_value():
    with pytest.raises(ValueError):
        is_natural(-100)
        logging.ERROR(f'Ошибка значения , отрицательнрое число {test_is_natural}')
def test_value_with_text():
    with pytest.raises(ValueError, match=r'Число А должно быть больше 1 '):
         is_natural(1)
         logging.ERROR(f'Ошибка значение , значение должно быть больше {test_is_natural}')
