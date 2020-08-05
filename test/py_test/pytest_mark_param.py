
import pytest

@pytest.mark.parametrize('n1',[1,3,5,6])
@pytest.mark.parametrize('n2',[2,4,6,8])
def test_is_odd_even(n1,n2):
    assert n1%2==1
    assert n2%2==0
    
