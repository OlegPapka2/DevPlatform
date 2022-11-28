from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128))

    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(80), unique=True, index=True, nullable=True)

    bio = db.Column(db.Text(), nullable=True)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    picture = db.Column(db.String(64), nullable=True)

    message = db.relationship("Message", back_populates="user")
    chats = db.relationship("Chat", secondary='chat_users', back_populates="users")

    @property
    def name(self) -> str:
        if self.username:
            name = f'@{self.username}'
        elif self.last_name:
            name = f'{self.first_name} {self.last_name}'
        else:
            name = f'{self.first_name}'

        return name

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(int(id))

    def __repr__(self):
        return f'<User {self.name}>'
