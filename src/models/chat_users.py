from extensions import db


class ChatUsers(db.Model):
    __tablename__ = 'chat_users'

    user_id = db.Column(db.Integer, db.ForeignKey("chat.id"), primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
