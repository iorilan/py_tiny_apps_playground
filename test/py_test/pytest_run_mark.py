"""
only run marked test
    pytest -v pytest_run_mark.py -m only_me
run all except marked test
    pytest -v pytest_run_mark.py -m 'not only_me'
"""

import pytest

@pytest.mark.only_me
def test_true():
    assert True

def test_false():
    assert False

def test_another_false():
    assert [1,2] == ('1','2')