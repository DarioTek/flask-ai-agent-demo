from .arithmetic import arithmetic_bp

def register_routes(app):
    app.register_blueprint(arithmetic_bp)
