import pytest
from yandex_request import pushing_files_to_yandex

@pytest.mark.xfail
def pushing_files_to_yandex():
    assert 0

class TestFunctionsPytest:
    def setup(self):
        print('setap')

    def teardown(self):
        print('teardown')

    def test_returning_name(self):
        assert pushing_files_to_yandex() == 201

