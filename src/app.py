from flask import Flask

from auth import auth_bp
from home import home_bp
from profile import profile_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(profile_bp)
