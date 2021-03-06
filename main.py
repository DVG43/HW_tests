import json
import os





documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def returning_name(alfa, dates):
    ansver_p = 0
    for personal_dates in dates:
        if personal_dates["number"] == alfa:
            return personal_dates["name"]
            ansver_p = 1
    if ansver_p == 0:
        print('Документа с таким номером нет')


def returning_directories(betta, shelfs):
    ansver_p = 0
    for namber_shelfs, list_doc in shelfs.items():
        if betta in list_doc:
            return namber_shelfs
            ansver_p = 1
    if ansver_p == 0:
        print('Документа с таким номером нет')


def returning_lis(dates):
    for personal_dates in dates:
        resultat = [personal_dates['type'], personal_dates['number'], personal_dates['name']]
        return resultat

def input_dates(t, n, np):
    new_dates = {"tape": t, "namber": n, "name": np}
    return new_dates


def shelfing(ns, n, shelf):
    if ns == 1:
        shelf['1'].append(n)
        return shelf
    elif ns == 2:
        shelf['2'].append(n)
        return shelf
    elif ns == 3:
        shelf['3'].app(n)
        return shelf

if __name__ == '__main__':
    print('команда p - выводит имя по номеру документа')
    print('команда s - выводит полку хранения по номеру документа')
    print('команда l - выводит весь лист хранения')
    print('команда а - добавляет новые данные')
    print('команда q - выход из программы')
    print()
    user_input = input('Введите команду  ')
    print()

    if user_input == 'p' and 'people':
        local_user_input = input('Введите номер документа ')
        print('имя', returning_name(local_user_input, documents))

    elif user_input == 's' and 'shelf':
        local_user_input = input('Введите номер документа ')
        print('номер полки', returning_directories(local_user_input, directories))

    elif user_input == 'l' and 'list':
        print(returning_lis(documents))

    elif user_input == 'a' and 'add':
        local_user_input_n = input('Введите номер документа  ')
        local_user_input_t = input('Введите тип документа  ')
        local_user_input_np = input('Введите имя владельца  ')
        documents.append(input_dates(local_user_input_t, local_user_input_n, local_user_input_np))

        while True:
            local_user_input_ns = int(input('Введите номер номер полки хранения '))
            if local_user_input_ns <= 3:
                break
            else:
                print('введен несуществующий номер полки')
        directories = shelfing(local_user_input_ns, local_user_input_n, directories)
    elif user_input == 'q':
        print('До свидания!')

    else:
        print('Не верный ввод команды')


