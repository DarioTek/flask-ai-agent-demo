import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_addition(client):
    resp = client.post('/arithmetic', json={"a": 2, "b": 3, "operation": "add"})
    assert resp.status_code == 200
    assert resp.get_json() == {"result": 5}

def test_subtraction(client):
    resp = client.post('/arithmetic', json={"a": 5, "b": 2, "operation": "subtract"})
    assert resp.status_code == 200
    assert resp.get_json() == {"result": 3}

def test_multiplication(client):
    resp = client.post('/arithmetic', json={"a": 4, "b": 3, "operation": "multiply"})
    assert resp.status_code == 200
    assert resp.get_json() == {"result": 12}

def test_division(client):
    resp = client.post('/arithmetic', json={"a": 10, "b": 2, "operation": "divide"})
    assert resp.status_code == 200
    assert resp.get_json() == {"result": 5.0}

def test_division_by_zero(client):
    resp = client.post('/arithmetic', json={"a": 10, "b": 0, "operation": "divide"})
    assert resp.status_code == 400
    assert resp.get_json() == {"error": "division by zero"}

def test_invalid_operation(client):
    resp = client.post('/arithmetic', json={"a": 1, "b": 2, "operation": "modulo"})
    assert resp.status_code == 400
    assert resp.get_json() == {"error": "unsupported operation"}

def test_missing_fields(client):
    resp = client.post('/arithmetic', json={"a": 1, "operation": "add"})
    assert resp.status_code == 400
    assert "error" in resp.get_json()

def test_non_json_body(client):
    resp = client.post('/arithmetic', data="not json", content_type='text/plain')
    assert resp.status_code == 400
    assert "error" in resp.get_json()

def test_non_number_input(client):
    resp = client.post('/arithmetic', json={"a": "foo", "b": 2, "operation": "add"})
    assert resp.status_code == 400
    assert "error" in resp.get_json()

def test_non_string_operation(client):
    resp = client.post('/arithmetic', json={"a": 1, "b": 2, "operation": 123})
    assert resp.status_code == 400
    assert "error" in resp.get_json()