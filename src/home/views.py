from flask import Blueprint, render_template
from flask_login import login_required

from extensions import login_manager

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
