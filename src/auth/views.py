from flask import render_template, Blueprint, redirect, url_for, request

from auth.forms import RegistrationForm
from models import User
from extensions import db
from utils.error_utils import flash_errors

auth_bp = Blueprint(
    'auth', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Log in user page"""
    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Register user page"""

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, email=form.email.data)
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    else:
        flash_errors(form)

    return render_template('registration.html', form=form)
