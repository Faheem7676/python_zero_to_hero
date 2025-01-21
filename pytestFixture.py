import pytest
@pytest.fixture()

def test_functionality():
    if not some_condition:
        pytest.skip("Some condition not met")
    assert my_function() == expected_value
    
    
@pytest.mark.parametrize("input, expected", [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected
    
@pytest.mark.parametrize("input,expected",[(1,2),(2,3),(3,4)])

def test_increment(input,expected):
    assert input+1==expected