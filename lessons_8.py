import json
import csv
from pathlib import Path
from typing import TextIO
import os
import pickle


# Задание No1
# 📌 Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

""""
def create_json(file: Path)-> None:
    file_data = {}
    with open(file, 'r' , encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            file_data[name.capitalize()]= float(number)
    with open(file.stem+'.json', 'w', encoding='utf-8') as f_2:
        json.dump(file_data, f_2, indent=2 , ensure_ascii=False)
"""

# Задание No2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

""""
def ask_data(name : str, personal_id: int, level: int)-> dict[int: dict[str, int]]:
    return {level: {personal_id,name}}

def write_json(data: dict)-> None:
    file = 'data.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False , indent=2)

def ui():
    exit_program = False
    print('Welcome to the programs, give me your date and i remembor this')
    while exit_program:
        personal_id = int(input('Введите ID: '))
        name = input('Введите имя: ')
        level = int(input('Введите уровень доступа: '))
        continue_program = input('Хотите продолжить? Да/Нет')
        if continue_program == 'нет':
            exit_program = True
        write_json(ask_data(name,personal_id,level))

def read_json('data.json', 'r', encoding='utf-8') as read_file:
    data = read_file.read()
    if not data:
        return {}
    del data
    data_from_file = json.load(read_file, object_hook=_decode)
    return data_from_file

def make_base (data_to_write: dict) :
    base_list = []
    read_data = read_json ()
    base_list.append (read_data)
    return base_list

"""

# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
#  - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

dir_list = os.listdir()


def read_dir(dir_list):
    for perents_dir, children_dir, file_object in os.walk(os.getcwd()):
        with open('file_dir.json', 'w+', encoding='utf-8') as f:
            perents_dir = json.load(f)
            children_dir = json.load(f)
            file_object = json.load(f)
        # with (
        #    open('file_read.csv', 'r', newline='') as f_read,
         #     open('file_dear_csv.csv', 'w+', newline='', encoding='utf-8') as f_write
       # ):
        #     perents_dir , children_dir , file_object = csv.reader(f_read, dialect='exel-tab',quoting=csv.QUOTE_NONNUMERIC)
    perents_dir = dict(perents_dir)
    children_dir = dict(children_dir)
    file_object = dict(file_object)
    with open('file_pikle.pickle', 'wb') as f:
        pickle.dump(perents_dir, f)
        pickle.dump(children_dir, f)
        pickle.dump(file_object, f)

    for children_dir in perents_dir:
        print(f'{perents_dir} родительская папка для {children_dir}')


print(read_dir(dir_list))
