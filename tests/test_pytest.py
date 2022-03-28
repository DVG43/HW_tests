import pytest
from main import returning_name, returning_directories,returning_lis

class TestFunctionsPytest:
    def setup(self):
        print('setap')

    def teardown(self):
        print('teardown')

    def test_returning_name(self):
        assert returning_name () ==

    def test_returning_directories(self):
        assert returning_directories () ==

    def test_returning_lis(self):
        assert returning_lis () ==