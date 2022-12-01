from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import Length, optional

from models import User


class ProfileEditForm(FlaskForm):
    email = StringField('email', validators=[optional(), Length(min=3, max=120)])
    first_name = StringField('first_name', validators=[optional(), Length(min=3, max=64)])
    last_name = StringField('last_name', validators=[optional(), Length(min=3, max=64)])
    nickname = StringField('nickname', validators=[optional(), Length(min=3, max=64)])
    bio = StringField('nickname', validators=[optional(), Length(min=3, max=128)])
    picture = FileField('picture', validators=[optional()])

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(ProfileEditForm, self).validate()
        if not initial_validation:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("E-mail already registered!")
            return False

        user = User.query.filter_by(username=self.nickname.data).first()
        if user:
            self.nickname.errors.append("Nickname taken!")
            return False

        return True
