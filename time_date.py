#Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
#Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
#Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
#Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
#Проверку года на високосность вынести в отдельную защищённую функцию.

from datetime import datetime

def _chek_yars_one(date: str)-> bool :
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400 
    YEARS= range(1,10000)
    year = int(date.split(' ')[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or yaer % CHECK_NORMAL_3 == 0:
        return True
    return False
     


    
def chek_years(year:str)-> bool:
    try:
        valuy = datetime.strftime(year, "%d/%m/%y").date()
        return True
    except:
        return False

def final_chek(date : str)-> bool:
    if chek_years(date):
        return _chek_yars_one(date)