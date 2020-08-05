import pytest
import os
"""
    autouse will make sure fixture executed before other test
"""

class Env:
    _prepared = False

@pytest.fixture(autouse=True)
def prepare():
    Env._prepared = True
    print('prepared')
    yield
    Env._prepared = False
    print('reset')

def test_ready():
    assert Env._prepared

def test_not_ready():
    assert not Env._prepared