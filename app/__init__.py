from flask import Flask
from app.routes.arithmetic import arithmetic_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(arithmetic_bp)
    return app
