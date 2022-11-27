from flask import Blueprint, render_template
from flask_login import login_required
from flask_socketio import send

from extensions import socketio

home_bp = Blueprint(
    'home', __name__,
    template_folder='templates',
    static_folder='static'
)


@home_bp.route('/', methods=['GET'])
@login_required
def index():
    """Home page"""
    return render_template('index.html')


@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    if message != "User connected!":
        send(message, broadcast=True)


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    send(json, broadcast=True)
