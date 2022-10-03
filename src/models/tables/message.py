from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, VARCHAR
from sqlalchemy.orm import relationship

from models.base import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey("user.id"), nullable=False)
    chat_id = Column(INTEGER, ForeignKey("chat.id"), nullable=False)
    date = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    text = Column(TEXT, nullable=True)
    picture = Column(VARCHAR(64), nullable=True)

    user = relationship("User", back_populates="message")
    chat = relationship("Chat", back_populates="message")
