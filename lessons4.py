# Напишите функцию для транспонирования матрицы

matr = [[1, 2], [3, 4]]


def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp+[matr[i][j]]
        res = res+[tmp]
    return res


print(transpose(matr))

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
#  используйте его строковое представление.

ammunition = dict(pen=1, blade=2, chikfier=1, whater=2, sleeping_bag=3, axe=4)


def ammunitions(**kwargs):
    for key in kwargs.items():
        res = kwargs.setdefault(kwargs(key))
    for values in kwargs.items():
        res = kwargs.setdefault(kwargs(values))
        return res


print(ammunitions(ammunition))
