#Задание No1
#📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
#📌 Экземпляр должен запоминать последние k значений.
#📌 Параметр k передаётся при создании экземпляра.
#📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

#Задание No2
#📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import collections
from typing import DefaultDict, Dict
import json
import csv

class My_funk:
    _context_dict = dict()
    def __init__(self,k):
        self.k = k
        self.save_list = list()
    
    def __call__(self, value):
        res = 1
        for i in range (2, value + 1):
            res *= i
        self.save_list.append (res)
        if len (self.save_list) > self.k:
            self.save_list.pop(0)
        return self.save_list[-1]
        
    def __str__(self):
        return f'Fact {self.save_list}'

    def __enter__(self):
        return self
    
    def mapper(self):
        for i , value in enumerate(self.save_list, start=1):
            self._context_dict[i] = value


    def __exit__(self, exc_type,exc_val, exc_tb):
        self.mapper()
        with open('json_res.json', 'w') as f:
            json.dump(self._context_dict,f, indent=2)

#Задание No3
#📌 Создайте класс-генератор.
#📌 Экземпляр класса должен генерировать факториал числа в
#диапазоне от start до stop с шагом step.
#📌 Если переданы два параметра, считаем step=1.
#📌 Если передан один параметр, также считаем start=1.

class FactGenerated:

    def __init__(self,*args):
        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args
        


    def __iter__(self):
        return self
    
    def __next__(self): 
        while self.start < self.stop:
            res = 1
            for j in range(2, self.start + 1):
                res *= j 
            self.start += self.step

            return res
            raise StopIteration

#Задание No4
#📌 Доработайте класс прямоугольник из прошлых семинаров.
#📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
#📌 Используйте декораторы свойств.

#Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

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
    def side_1(self,value):
        if value > 0:
            self.side_1= value
        else:
            raise ValueError('Введите положительное число')
    
    @side_2.setter
    def side_2(self,value):
        if value > 0:
            self.side_2= value
        else:
            raise ValueError('Введите положительное число') 
        

    def area(self):
        '''Подсчет площади прямоугольника'''
        return self.side_2 * self.side_1
    #print(area.__doc__)

    def perimetr(self):
        '''Подсчет периметра прямоугольника'''
        return 2 * (self.side_1 + self.side_2)
    #print(perimetr.__doc__)

    def __add__(self, other):
        '''Подсчет стороны прямоугольника из его площади '''
        new_perimetr = self.perimetr() + other.perimetr()
        new_a = self.side_1
        new_b = new_perimetr / 2 - new_a
        return Rectangle(new_a, new_b)
    #print(__add__.__doc__)

    def __sub__(self, other):
        new_perimetr = abs(self.perimetr() + other.perimetr())
        new_a = min([self.side_1, self.side_2, other.side1, other.side2])
        new_b = new_perimetr / 2 - new_a
        return Rectangle(new_a, new_b)
    #print(__sub__.__doc__)


#Создайте класс студента. 
#* Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. 
#* Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. 
#* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). 
#* Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

class Student:

   def __init__(self,fullname,name_stady,test_ball,grade):
        self.fullname = fullname
        self.name_stady =name_stady
        self.test_ball = test_ball
        self.grade = grade 

    def __get__(self):
        









        

