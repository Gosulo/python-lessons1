import time

# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)


class My_str(str):
    """Расширяем класс str. """
    def __new__(cls, value, name):
        '''Расширение метод new параметр value and name.'''
        instanse = super().__new__(cls, value)
        instanse.name = name
        instanse.created_at = time.time()
        return instanse
    print(__new__.__doc__)


# 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров
# сохраняются в пару списков- архивов
# 📌 list-архивы также являются свойствами экземпляра
# Добавить метод представление экзкмпляра для програмиста и пользователя


class Archive:
    ''' Cохраненине данных каждого экземпляра класса в список numbers and values.'''
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        '''Переопределение метода new сохранение аргументов в список. '''
        cls.numbers.append(number)
        cls.values.append(value)
        instance = super() . __new__(cls)
        instance.numbers = [number]
        instance. values = [value]
        return instance
    print(__new__.__doc__)

    def __init__(self, number, value):
        '''Иницилизация значений number and value'''
        self.number = number
        self.value = value

    def __repr__(self):
        '''Вывод значений для разработчика'''
        return f'Arhive ({self.numbers} , {self.values})'
    print(__repr__.__doc__)

    def __str__(self) -> str:
        '''Вывод значения для пользователя'''
        return f'Номер: {self.numbers}\n Значение : {self.values}'
    print(__str__.__doc__)


# • Дорабатываем класс прямоугольник из прошлого семинара.
# • Добавьте возможность сложения и вычитания.
# • При этом должен создаваться новый экземпляр прямоугольника.
# • Складываем и вычитаем периметры, а не длинну и ширину.
# • При вычитании не допускайте отрицательных значений.

class Rectangle:
    '''Класс подсчета площади и периметра прямоугольника'''

    def __init__(self, side_1, side_2=None):
        '''Иницилизация сторон прямоугольника'''
        self.side_1 = side_1
        self.side_2 = side_2 if side_2 is not None else side_1

    def area(self):
        '''Подсчет площади прямоугольника'''
        return self.side_2 * self.side_1
    print(area.__doc__)

    def perimetr(self):
        '''Подсчет периметра прямоугольника'''
        return 2 * (self.side_1 + self.side_2)
    print(perimetr.__doc__)

    def __add__(self, other):
        '''Подсчет стороны прямоугольника из его площади '''
        new_perimetr = self.perimetr() + other.perimetr()
        new_a = self.side_1
        new_b = new_perimetr / 2 - new_a
        return Rectangle(new_a, new_b)
    print(__add__.__doc__)

    def __sub__(self, other):
        new_perimetr = abs(self.perimetr() + other.perimetr())
        new_a = min([self.side_1, self.side_2, other.side1, other.side2])
        new_b = new_perimetr / 2 - new_a
        return Rectangle(new_a, new_b)
    print(__sub__.__doc__)

# Домащнее задание
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица.
# Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,


class Matrix:

    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def matrix_sum(self):
        return summa(self.matrix_1 + self.matrix_2)

    def comparison_matrix(sefl):
        return print('Равны' if self.matrix_1 == self.matrix_2 else 'Не равны')


# if __name__=='__main__':
    # mystr=My_str('Строка','I_am')
    # print(mystr.name)
    # print(mystr.created_at)
    # print(mystr)
    # print(mystr.upper())

    # a_1=Archive(1,'One')
    # a_2=Archive(2,'Two')
    # print(f'{a_1.numbers }, {a_1.values }')
    # print(f'{a_2.numbers }, {a_2.values }')
    # print(a_1.__repr__())
    # print(f'{a_1 =}') # Альтернативный вариант вызова из 58 строки
    # print(a_1)
    # rect1 = Rectangle(2 , 5)
    # rect2 = Rectangle(5 , 10 )
    # print(f'{rect1.area()=},{rect1.perimetr()=}')
    # print(f'{rect2.area()=},{rect2.perimetr()=}')
    # res_sum = rect1 + rect2
    # print(res_sum.side_1 , res_sum.side_2)
    # res_sub = rect1 - rect2

    mat = Matrix[[12, 6, 8],
                 [8, 4, 33]

                 ]

    print(mat)
