from datetime import datetime

from extensions import db


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), nullable=False)
    date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    text = db.Column(db.Text(), nullable=False)

    user = db.relationship("User", back_populates="message")
    chat = db.relationship("Chat", back_populates="message")

    def __repr__(self):
        return f'<Message {self.id}>'
