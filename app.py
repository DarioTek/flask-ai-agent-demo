FILE: app/routes/health.py
from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

FILE: app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.health import health_bp
    app.register_blueprint(health_bp)

    return app

FILE: app/routes/__init__.py

FILE: tests/__init__.py

FILE: tests/test_routes.py
from app import create_app

def test_health_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "ok"}