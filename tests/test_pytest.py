import pytest
from main import returning_name, returning_directories, returning_lis

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