
from _typeshed import Self
from math import pi
import random
import string

# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, side_1, side_2=None):
        self.side_1 = side_1
        self.side_2 = side_2 if side_2 is not None else side_1

    def area(self):
        return self.side_2 * self.side_1

    def perimetr(self):
        return 2 * (self.side_1 + self.side_2)


# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании земпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def long(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * pow(self.radius, 2)

# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.


class Human:

    def __init__(self, name, lastname, age, gender):
        self.name = name
        self.lastname = lastname
        self.__age = age
        self.gender = gender

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self) -> str:
        return f'{self.name=} {self.lastname=} {self.get_age()=} {self.gender=}'

# Задание No4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь


class Sontudnik(Human):

    def __init__(self, name, lastname, age, gender, major,):
        super().__init__(name, lastname, age, gender)
        self.major = major
        self.emp_id = self._get_number()
        self.sec_level = self._secure_level()

    def _get_number(self):
        MIN_NUM = 1000000
        MAX_NUM = 1999999
        return random.randint(MIN_NUM, MAX_NUM)

    def _secure_level(self):
        LEVEL_NUM = 7
        sec_id = self._get_number()
        level_num = 0
        while sec_id > 0:
            last_num = sec_id % 10
            level_num += last_num
            sec_id /= 10
        return level_num % LEVEL_NUM

    def __str__(self) -> str:
        return f'{self.name=} {self.lastname=} {self.get_age()=} {self.gender=} {self.major=} {self.emp_id=}'

# Задание No5
# • Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# • У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# •Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
# 📌 Вынесите общие свойства и методы классов в класс Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.


class Animal:

    def __init__(self, name, weigt, age):
        self.name = name
        self.weigt = weigt
        self.age = age

    def move():
        pass

    def say():
        pass


class Birds(Animal):

    def __init__(self, name, weigt, age, type_bird, sound):
        super().__init__(name, weigt, age)
        self.type_bird = type_bird
        self._sound = sound

    def move(self):
        return 'Fly'

    def say(self):
        return self._sound

    def _str__(self):
        return f"{super ()} {self.type_bird} {self._sound}"


class Dog(Animal):

    def __init__(self, name, weigt, age, type_dog,):
        super().__init__(name, weigt, age)
        self.type_dog = type_dog

    def move(self):
        return 'Run'

    def say(self):
        return 'Gov'

    def _str__(self):
        return f"{super ()} {self.type_dog} {self.say}"


class Fish(Animal):

    def __init__(self, name, weigt, age, fish_type):
        super().__init__(name, weigt, age)
        self.fish_type = fish_type

    def move(self):
        return 'swimming'

    def say(self):
        return 'None'

    def _str__(self):
        return f"{super ()} {self.fish_type} {self.say}"


# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Fabrika(Dog):

    def __init__(self, name, weigt, age, type_dog):
        super().__init__(name, weigt, age, type_dog)

    def move(self):
        return 'Run'

    def say(self):
        return 'Gov'

    def __str__(self) -> str:
        return super().__str__()

# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.


class Clear_text:

    def __init__(self, text):
        self.text = text

    def text_clears(self):
        for p in string.punctuation + '\n':
            if p in self.text:
                text = self.text.replace(p, ' ')
            return text

    def counter(list_element):
        count = {}
        for element in list_element:
            if count.get(element, None):
                count[element] += 1
            else:
                count[element] = 1

        sorted_values = sorted(
            count.items(), key=lambda tpl: tpl[1], reverse=True)
        return dict(sorted_values)
    ext = text_clears(Self.text.lower())
    list_world = Self.text.split()
    print(counter(list_world))


if __name__ == '__main__':
    # Number 1
    # circle = Circle()
    # print(f'{circle.long() =} , {circle.area() =}')
    # rect1 = Rectangle(10 , 20)
    # rect2 = Rectangle(10)

    # print(f'{rect1.area()=},{rect1.perimetr()=}')
    # print(f'{rect2.area()=},{rect2.perimetr()=}')

    # Number 2
    # h_1 =  Human('Виктор','Viktorovich',35, 'Man')
   # h_2 =  Human('Bob','Marli',12, 'Man')
    # print(h_1)
    # print(h_2)

    # Number 3
    # h_1.birthday()
    # h_2.birthday()
    # print(h_1)
    # print(h_2)

    # Задача 4
    # eml_1 = Sontudnik('Vitu','Morisst',30,'Man','BOSS')
    # print(eml_1)

 # text=Clear_text()
 # print(text)

    dog_fabrik = Fabrika('Buba', 10, 12, 'Doberman')
    print(dog_fabrik)
