from .auth_views import auth_bp
from .perfume_view import perfume_bp

def register_bp(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(perfume_bp)
