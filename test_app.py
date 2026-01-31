import pytest
from app import app

def test_health_status_code():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_health_json_response():
    client = app.test_client()
    response = client.get("/health")
    assert response.is_json
    assert response.get_json() == {"status": "ok"}