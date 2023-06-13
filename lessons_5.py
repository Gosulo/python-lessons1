# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


from re import split
from types import ClassMethodDescriptorType


text = 'Users/georgiy/Desktop/Док24/doct24_iOS_3709/Doctor24/Common/InfoDev.plist'
*link, suffix = text.split('/')
file_name, file_format = suffix.split('.')
print(f',{link = } , {file_name = }, {file_format = } ')


def my_link(text):
    *link, suffix = text.split('/')
    file_name, file_format = suffix.split('.')
    my_tuple = link, file_name, file_format
    return my_tuple


print(my_link(text))


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
#  имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

name = ['Anna', 'Oleg', 'Polina', 'Kim']
bid = [112, 40, 75, 1100]
bonus = ['10.25', '12.50', '50.50', '5.75']

my_gen = {name: name for (name, (float(bid) * bonus)) in name}

print(my_gen)
