# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами.
# (3-7 строк импорта).

from math import pi as pp
from sys import argv
import select as lect
from random import randint as run, random
import my_modul
import zagadka
import time_date


# my_modul.game(1,10,3)
#try_count = zagadka.puzzle('Зимой и летом одним цветом',['Елочка','Ель','Елка','Пихта'], 5)
#print(f'Угадано за {try_count}')

data = '11.03.1987'

print(time_date.chek_years(data))


if __name__ == '__main__':
    _, *arg = argv

  #  my_modul.game(*(int(i) for i in argv[1:]))


