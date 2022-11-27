from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask_socketio import send, join_room, leave_room

from extensions import socketio

home_bp = Blueprint(
    'rooms', __name__,
    template_folder='templates',
    static_folder='static'
)


@home_bp.route('/rooms', methods=['GET'])
@login_required
def rooms():
    """Home page"""
    user_id = current_user.id

    return render_template('rooms.html')


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)


@socketio.on('message')
def handle_message(data):
    print(f"Received message: {data}")
    room = data['room']
    send(data, to=room)


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    send(json, broadcast=True)
