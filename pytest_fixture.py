import pytest

@pytest.fixture

def sample_data():
    
    return {"name": "John","age": 43}

# use the fixture in a test function
def test_sample_data(sample_data):
    
    assert sample_data["name"]=="john"
    assert sample_data["age"]==30
    
    