"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from csv import DictReader, DictWriter
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя')
            second_name = input('Введите фамилию: ')
            if len(second_name) < 4:
                raise NameError('Слишком короткая фамилия')
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) < 11:
                raise NameError('Слишком короткий номер телефона')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()

def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    standart_write(file_name, res)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)  # список со словарями

def remove_row(file_name):
    search = int(input('Введите номер строки для удаления: '))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search - 1)
        standart_write(file_name, res)
    else:
        print('Введен неверный номер строки')

def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)

def copy_data(src_file, dest_file):
    # Запрашиваем у пользователя номер строки для копирования
    row_number = int(input('Введите номер строки для копирования: '))
    # Читаем данные из исходного файла
    src_data = read_file(src_file)

    # Проверяем, существует ли строка с указанным номером
    if 1 <= row_number <= len(src_data):
        row_to_copy = src_data[row_number - 1]
        # Читаем данные из файла назначения
        dest_data = read_file(dest_file)
        # Добавляем строку к данным файла назначения
        dest_data.append(row_to_copy)
        # Записываем обновленные данные в файл назначения
        standart_write(dest_file, dest_data)
        print(f'Строка {row_number} успешно скопирована из {src_file} в {dest_file}')
    else:
        print('Введен неверный номер строки')


file_name = 'phone.csv'
def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутсвует, пожалуйста создайте файл')
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print('Файл отсутсвует, пожалуйста создайте файл')
                continue
            remove_row(file_name)
        elif command == 'c':
            src_file = input('Введите имя исходного файла: ')
            dest_file = input('Введите имя файла назначения: ')
            if not exists(src_file):
                print('Исходный файл отсутствует')
                continue
            if not exists(dest_file):
                create_file(dest_file)
            copy_data(src_file, dest_file)
main()


"""
реализовать копирование данных из файла А в файл B.
написать отдельную функцию copy_data:
прочитать список словарей (read_file)
и записать его в новый файл используя функцию standart_write
дополнить функцию main
"""