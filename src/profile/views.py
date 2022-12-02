import os.path

from flask import Blueprint, render_template, url_for, flash
from flask_login import login_required, current_user
from flask_socketio import emit
from werkzeug.utils import secure_filename

from config import Config
from extensions import db, socketio
from models import User
from profile.forms import ProfileEditForm
from utils.error_utils import flash_errors

profile_bp = Blueprint(
    'profile', __name__,
    template_folder='templates',
    static_folder='static'
)


@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """User profile page"""

    user = User.get_by_id(current_user.get_id())

    form = ProfileEditForm()
    if form.validate_on_submit():
        if form.email.data != user.email and form.email.data != '':
            user.email = form.email.data

        if form.first_name.data != user.first_name and form.first_name.data != '':
            user.first_name = form.first_name.data

        if form.last_name.data != user.last_name and form.last_name.data != '':
            user.last_name = form.last_name.data

        if form.nickname.data != user.username and form.nickname.data != '':
            user.username = form.nickname.data

        if form.bio.data != user.bio and form.bio.data != '':
            user.bio = form.bio.data

        if filename := secure_filename(form.picture.data.filename):
            form.picture.data.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            user.picture = filename

        db.session.commit()
    else:
        flash_errors(form)

    profile_picture = current_user.picture

    if profile_picture:
        picture_path = url_for('static', filename=f'profile_pictures/{profile_picture}')
    else:
        picture_path = url_for('static', filename='profile_pictures/default_profile_picture.png')

    return render_template('profile.html', profile_picture=picture_path, form=form)


@socketio.on('delete_image')
def handle_my_custom_event():
    user = User.get_by_id(current_user.get_id())
    old_pic = user.picture
    default_picture = 'default_profile_picture.png'

    if old_pic != default_picture:
        user.picture = default_picture
        db.session.commit()

        emit('change_image', {"image_path": url_for('static', filename=f'profile_pictures/{default_picture}')})
        os.remove(f'static/profile_pictures/{old_pic}')
