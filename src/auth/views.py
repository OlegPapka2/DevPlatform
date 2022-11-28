from flask import render_template, Blueprint, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user

from auth.forms import RegistrationForm, LoginForm
from models import User
from extensions import db, login_manager
from utils.error_utils import flash_errors

auth_bp = Blueprint(
    'auth', __name__,
    template_folder='templates',
    static_folder='static'
)


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Log in user page"""

    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash('Logged in successfully.')
            return redirect(url_for('rooms.home'))
        else:
            flash_errors(form)

    return render_template('login.html', form=form)


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


@auth_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    """Logout user."""

    logout_user()
    flash("You are logged out.", "info")

    return redirect(url_for("auth.login"))
