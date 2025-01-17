import pytest

@pytest.fixture
@pytest.fixture(params=["data1","data2"])

def set_teardown():
    
    # setUp
    resource={"status": "initiazed"}
    yield resource
    
    # Teardown
    resource["status"]="cleaned up"
    
    
def test_resource_status(set_teardown):
    
    assert set_teardown["status"]=="initialized"
    
# parameterized Fixture



def data__variants(request):
    
    return request.param


def test_data_variants(data_variants):
    
    assert data_variants in ["data1", "data2"]