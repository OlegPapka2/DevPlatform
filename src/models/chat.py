from app import db


class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    private = db.Column(db.Boolean, nullable=False, default=True)

    users = db.relationship("User", secondary='chat_users', back_populates="chats")
    message = db.relationship("Message", back_populates="chat")

    def __repr__(self):
        return f'<Chat {self.id}>'
