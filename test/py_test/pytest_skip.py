#pytest -v pytest_skip.py

import pytest
import datetime

_skip_randomly= datetime.datetime.now().time().second%2==0

def test_true():
    assert True

@pytest.mark.skipif(_skip_randomly,reason="sometime skip it")
def test_false():
    print('didnt skip')
    assert False

def test_another_false():
    pytest.skip("always skiping at runtime")
    assert [1,2] == ('1','2')