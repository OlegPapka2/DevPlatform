from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import INTEGER

from models.base import Base


class ChatUsers(Base):
    __tablename__ = 'chat_users'

    user_id = Column(INTEGER, ForeignKey("chat.id"), primary_key=True)
    chat_id = Column(INTEGER, ForeignKey("user.id"), primary_key=True)
