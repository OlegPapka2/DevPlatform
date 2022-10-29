from flask import Flask

from auth import auth_bp
from extensions import db
from home import home_bp
from profile import profile_bp


def register_extensions(app):
    """Register Flask extensions"""
    db.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints"""
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(profile_bp)


def create_app():
    """Create application factory"""
    app = Flask(__name__)
    app.config.from_object('config.Config')
    register_extensions(app)
    register_blueprints(app)
    return app


app = create_app()
