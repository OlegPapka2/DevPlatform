from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR
from sqlalchemy.orm import relationship

from models.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    first_name = Column(VARCHAR(64), nullable=False)
    last_name = Column(VARCHAR(64), nullable=True)
    nickname = Column(VARCHAR(20), nullable=False)
    picture = Column(VARCHAR(64), nullable=True)

    message = relationship("Message", back_populates="user")
    chats = relationship("Chat", secondary='chat_users', back_populates="users")
