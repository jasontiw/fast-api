from unittest import result
from fastapi.testclient import TestClient
from main import app    

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
    
def test_rate_conversion_usd_to_usd():
    response = client.get("/conversion?org=USD&dest=USD&amount=1")
    assert response.status_code == 200
    result = response.json();
    assert result['data'] == 1
    
def test_rate_conversion_usd_to_col():
    response = client.get("/conversion?org=USD&dest=COL&amount=1")
    assert response.status_code == 200
    result = response.json();
    assert result['data'] == 3930.55
    