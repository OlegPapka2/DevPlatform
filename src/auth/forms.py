from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(min=3, max=120)])
    first_name = StringField('first_name', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=1, max=64)])
    password_confirmation_validators = [DataRequired(), EqualTo('password', message='Passwords must match')]
    password_confirmation = PasswordField('password_confirmation', validators=password_confirmation_validators)

