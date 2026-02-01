from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.arithmetic import arithmetic_bp
    app.register_blueprint(arithmetic_bp)

    # Register other blueprints/routes here if needed

    return app
