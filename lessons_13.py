

#Задание No1
#📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
#📌 Обрабатывайте не числовые данные как исключения.

def give_number():
    while True:
        num = int(input('Give me number: '))
        try:
            #if isinstance(num, (int,float)):
            num =float(num)
            break
        
        except ValueError as e:
            print(f'Вы ввели неправильное значение: {e}\n Попробуй снова')
    try:
        num = int(num)
            break
    except ValueError as e:
    print(f'Вы ввели неправильное значение: {e}\n Попробуй снова')
            

#Задание No2
#📌 Создайте функцию аналог get для словаря.
#📌 Помимо самого словаря функция принимает ключ и значение по умолчанию.
#📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
#📌 Реализуйте работу через обработку исключений.

def get_default(data: dict, key , value = 1):

    try:
        result = data[key]
    except KeyError as e:
        result = value
        return result


#Задание No3
#📌 Создайте класс с базовым исключением и дочерние классы- исключения:
#○ ошибка уровня,
#○ ошибка доступа.

class Castom:
    pass


class LevelError:
    pass


class AccesseError:
    pass



#Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

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
        try:
            self.side_1 < 0
        except ValueError as e:
            print(f'Сторона не может быть отрицательной')
            self.side_1= 1
            print(f'Будем считать результатом число {self.side_1}')
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