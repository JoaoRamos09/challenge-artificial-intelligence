from sqlalchemy import Column, String, DateTime, Integer, Enum
from sqlalchemy.orm import relationship
from app.backend.enum.status_conversation_enum import StatusConversationEnum
from datetime import datetime
from app.backend.database.base import Base

class ConversationSchema(Base):
    __tablename__ = "conversations"
    
    id = Column(String, primary_key=True)
    user_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    finished_at = Column(DateTime)
    status = Column(Enum(StatusConversationEnum), default=StatusConversationEnum.START, nullable=False)
    messages = relationship("MessageSchema", back_populates="conversation")
    