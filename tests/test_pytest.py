import pytest
from main import returning_name, returning_directories, returning_lis
from yandex_request import pushing_files_to_yandex

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


class TestFunctionsPytest:
    def setup(self):
        print('setap')

    def teardown(self):
        print('teardown')

    def test_returning_name(self):
        assert returning_name("11-2", documents) == "Геннадий Покемонов"

    def test_returning_directories(self):
        assert returning_directories ("11-2", documents) == '10006'

    def test_returning_lis(self):
         assert returning_lis (documents) == ['passport', '2207 876234', 'Василий Гупкин']