"""
    -use fixture to share test context cross all test
    -spcifying sharing scope
"""
import pytest

@pytest.fixture(scope="module")
def context():
    print('creating context object')
    yield ['some','dummy','context']
    print('disposed context object.')

def test_true(context):
    print(context)
    assert True

def test_false(context):
    print(context)
    assert False

def test_another_false(context):
    print(context)
    assert [1,2] == ('1','2')