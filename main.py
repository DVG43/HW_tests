import json
import os


# При наличии своего решения данной задачи можно использовать его или использовать предложенный код в директории scr текущего задания.
#
# * Следует протестировать основные функции по получению информации о документах, добавлении и удалении элементов из словаря.
# * Используйте fixture для загрузки данных в тестовый класс.
#
# Рекомендации по тестам.
# 1. Если у вас в функциях информация выводилась(print), то теперь её лучше возвращать(return) чтобы можно было протестировать.
# 2. Если есть проблемы с input в тестах, то лучше переписать функции так, чтобы данные приходили через параметры.
# 2. input можно "замокать" с помощью ```unittest.mock.patch```, если с этим будут проблемы, то лучше переписать функции так, чтобы данные приходили через параметры.
#
# ### Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
#   24  4.Tests/src/app.py
# @@ -1,17 +1,14 @@
# Домашнее задание к лекции 2.1 «Функции — использование встроенных и создание собственных»

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]


def update_date():
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    f_directories = os.path.join(current_path, 'fixtures/directories.json')
    f_documents = os.path.join(current_path, 'fixtures/documents.json')
    with open(f_documents, 'r') as out_docs:
        documents = json.load(out_docs)
    with open(f_directories, 'r') as out_dirs:
        directories = json.load(out_dirs)
    return directories, documents
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def check_document_existance(user_doc_number):
@@ -174,6 +171,5 @@ def secretary_program_start():
            break


directories, documents = update_date()
if __name__ == '__main__':
    secretary_program_start()
