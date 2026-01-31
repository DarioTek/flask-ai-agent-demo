import pytest
from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route('/health')
    def health():
        return {"status": "ok"}, 200

    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_status_code(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_health_json_response(client):
    response = client.get('/health')
    data = response.get_json()
    assert data == {"status": "ok"}