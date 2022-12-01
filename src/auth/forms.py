from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length, EqualTo

from models import User


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(min=3, max=120)])
    first_name = StringField('first_name', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=1, max=64)])
    password_confirmation_validators = [DataRequired(), EqualTo('password', message='Passwords must match')]
    password_confirmation = PasswordField('password_confirmation', validators=password_confirmation_validators)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(RegistrationForm, self).validate()
        if not initial_validation:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("E-mail already registered")
            return False

        return True


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(min=3, max=120)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=1, max=64)])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(email=self.email.data).first()
        if not self.user:
            self.email.errors.append("Unknown e-mail")
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append("Invalid password")
            return False

        return True
