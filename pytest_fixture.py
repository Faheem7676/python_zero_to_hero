# Importing the math and pytest libraries
import pytest
import math

# @pytest.fixture

# def sample_data():
    
#     return {"name": "John","age": 43}

# # use the fixture in a test function
# def test_sample_data(sample_data):
    
#     assert sample_data["name"]=="john"
#     assert sample_data["age"]==30
    
# Creating the common function for input
@pytest.fixture
def input_value():
    
    input=8
    return input

# creating first test case

def test_check_difference(input_value):
    
    assert 99-93==input_value
    
# Creating second test case
def test_check_square_root(input_value):
   assert input_value==math.sqrt(64)
    
    