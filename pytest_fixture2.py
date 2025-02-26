import pytest

@pytest.fixture

def setup_data():
    
    print("\nSetting up test data...")
    
    return {"username":"Test_user","password":"secure123"}


def test_login(setup_data):
    
    print("Using fixture data:", setup_data)
    assert setup_data["username"]=="Test_user"
    assert setup_data["password"]=="secure123"   