from sqlalchemy import Column, BOOLEAN
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR
from sqlalchemy.orm import relationship

from models.base import Base


class Chat(Base):
    __tablename__ = 'chat'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(64), nullable=False)
    private = Column(BOOLEAN, nullable=False, default=True)

    users = relationship("User", secondary='chat_users', back_populates="chats")
    message = relationship("Message", back_populates="chat")
