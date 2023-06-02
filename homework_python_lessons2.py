
# 1 задание. 
# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

a = 5 
b = 12.5
c = 'Open'
d = (11,25,11.6,14)
e = {1: 3}
print(type(a),type(b),type(c),type(d), sep='\n')



#Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных 
# скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
 # ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.#

date = [a,b,c,d,5,'Open']
for i , el in enumerate(date):
    print(i + 1 , el , id(el), el.__sizeof__(), hash(el))
    if isinstance(el, int):
        print('Это целое число')
    elif isinstance(el, str):
        print('Это строка')
        

# Задание No3
# ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
#в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


def task3(num: int) -> str:
    result = ''
    res = None
    while num >=  1:
     res = num % 2
     result += str(res)
     num = num // 2
    return result [:: -1] 

print(task3(15), bin(15))



#Задание No4
# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.


def cicrle(d : float ) -> tuple[float,float]:
    if d < 1000:
     pi: float = 3.14 
     s : float = (pi * d **2) / 4
     l = 2 * pi *(d / 2)
     return float(s),float(l)

print(cicrle(3))


# Задание No6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


class BANK:

 balanse = 0 
 MULTIPLE = 50 # Кратность 
 COMISSION = 0.015
 COMISSION_MIN = 30
 COMISSION_MAX = 600
 BONUS = 0.03
 TAX = 0.10
 count_operetion = int
 
 def __init__(self) -> None:
     self.count_operetion = 0

 def put_money(self, cash):
    if cash % self.MULTIPLE == 0:
        self.balanse += cash
        self.count_operetion += 1 
    return self.balanse, self.count_operetion
 
 def take_moey(self, cash):
     if cash % self.COMISSION == 0 and self.balanse > 0 and self.balanse - (cash * self.COMISSION) > 0:
         self.balanse -= cash 
         self.count_operetion += 1
     return self.balanse, self.count_operetion
        
def exit(self):
    return 'Good bay'

def start(self, mode : str, cash: int) -> str: 
    match mode:
        case 'put_money':
            self.put_money(cash=cash)
        case 'take_money':
            self.take_money(cash=cash)
        case 'exit':
            self.exit()


#Домашнее задание
#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое 
#представление. Функцию hex используйте для проверки своего результата.#


def heex(num : int ) -> str:
    result = ''
    res = None
    while num >= 1 :
        res = num % 16
        result += str(res)
        num = num // 16 
        reversedstring =''.join(reversed(result))
    return reversedstring
print(heex(1111), hex(1111)) #Осталося только вопрос , как сюда привязать алфавит 



#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
from math import gcd
n1 , d1  = map(int,input('Введите первую дробь:').split('/'))
n2 , d2  = map(int,input('Введите вторую дробь:').split('/'))

if d1 == d2:
    print('{}/{}'.format(n1 + n2,d2))
    print('{}/{}'.format(n1 * n2,d1 * d2))
else:
    cd = int(d1*d2/gcd(d1, d2))
    rn = int(cd/d1*n1+cd/d2*n2)
    g2 = gcd(rn, cd)
    n = int(rn/g2)
    d = int(cd/g2)
    print('{}/{}'.format(n, d) if n != d else n)
    print('{}/{}'.format(n1 * n2,d1 * d2))

fractions_summ = Fraction(n1,d1) + Fraction(n2,d2)
fractions_pro = Fraction(n1,d1) * Fraction(n2,d2)
print(fractions_summ,fractions_pro)










