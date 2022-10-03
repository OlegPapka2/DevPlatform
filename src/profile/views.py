from flask import Blueprint, render_template

profile_bp = Blueprint(
    'profile', __name__,
    template_folder='templates',
    static_folder='static'
)


@profile_bp.route('/profile', methods=['GET'])
def profile():
    """User profile page"""
    return render_template('profile.html')
