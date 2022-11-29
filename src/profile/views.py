from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

profile_bp = Blueprint(
    'profile', __name__,
    template_folder='templates',
    static_folder='static'
)


@profile_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    """User profile page"""

    profile_picture = current_user.picture

    if profile_picture:
        picture_path = url_for('static', filename=f'profile_pictures/{profile_picture}')
    else:
        picture_path = url_for('static', filename='profile_pictures/default_profile_picture.png')

    return render_template('profile.html', profile_picture=picture_path)
