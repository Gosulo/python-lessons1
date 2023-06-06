# Задача 1 Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


my_list = [2, 3, 41, 2, 11, 23, 3, 41]
new_list = [list]
new_list_duble = []
lenlist = len(my_list) - 1
i = 0
j = 0

while i < lenlist:
    if my_list[j] == my_list[i]:
        new_list_duble.append(my_list[j])
        i += 1
    else:
        new_list.append(my_list[j])
        i += 1
        j += 1
print(new_list, new_list_duble, sep='\n')


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#  Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.


text = 'Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование[25], метапрограммирование[29] и функциональное программирование[25]. Задачи обобщённого программирования решаются за счёт динамической типизации[30][31]. Аспектно-ориентированное программирование частично поддерживается через декораторы[32], более полноценная поддержка обеспечивается дополнительными фреймворками[33]. Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений[34]. Основные архитектурные черты — динамическая типизация, автоматическое управление памятью[25], полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL)[35], высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты[36].'


def text_clear(text):
    import string
    for p in string.punctuation + '\n':
        if p in text:
            text = text.replace(p, ' ')
            return text


def counter(list_element):
    count = {}
    for element in list_element:
        if count.get(element, None):
            count[element] += 1
        else:
            count[element] = 1

    sorted_values = sorted(count.items(), key=lambda tpl: tpl[1], reverse=True)
    return dict(sorted_values)


text = text_clear(text.lower())
list_world = text.split()
print(counter(list_world))


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант

ammunition = dict(pen=1, blade=2, chikfier=1, whater=2, sleeping_bag=3, axe=4)
bag = 5

sorted_ammunition = dict(sorted(ammunition.items(), key=lambda x: -x[-1]))
for k, v in ammunition.items():
    if v <= bag:
        print(k, sep='\n')
        bag -= v
