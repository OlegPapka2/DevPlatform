from flask import render_template, Blueprint

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
    return render_template('registration.html')
