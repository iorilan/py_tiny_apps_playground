#pytest -v pytest_true.py

import pytest
def test_true():
    assert True

def test_false():
    assert False

def test_another_false():
    assert [1,2] == ('1','2')