# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и
# пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

import random


def game(min: int = 1, max: int = 10, try_count: int = 3) -> bool:
    res = False
    num = random.randint(min, max + 1)
    seach_count = 0
    while seach_count < try_count:
        ask_number = int(input(f'Введите число от {min} до {max}:'))
        if num == ask_number:
            res = True
            print(f'Вы угадали!Загаданное число {ask_number}')
            break
        if ask_number > num:
            print('Введеное число больше загаданного')
        else:
            print('Введеное число меньше  загаданного')
        seach_count += 1
    else:
        print('Попытки закончились')
    return res



