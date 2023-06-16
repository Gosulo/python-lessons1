#Создайте модуль с функцией внутри. 
#Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток 
# на угадывание.
#Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.





def puzzle(text : str , answers : list[str], try_count: int):
    print(text)
    count_tryding = 0 

    while count_tryding <= try_count:
        answer = input('Whot is it?')
        if answer in answers:
            print('YES')
            break
        else:
            print('NO, think more ')
            count_tryding +=1
    return count_tryding