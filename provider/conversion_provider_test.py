from unittest import result
from fastapi.testclient import TestClient
from main import app    
# from conversion_provider as conversion_provider
import provider.conversion_provider as conversion_provider 


def test_get_conversion():
    response = conversion_provider.get_conversion("USD","USD",1)
    assert response == 1
    