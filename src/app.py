from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from auth import auth_bp
from home import home_bp
from profile import profile_bp

app = Flask(__name__)

app.config.from_object('config.Config')
db = SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(profile_bp)
