from sqlalchemy import Column, String, DateTime, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.enum.status_conversation_enum import StatusConversationEnum
from datetime import datetime

Base = declarative_base()

class ConversationSchema(Base):
    __tablename__ = "conversations"
    
    id = Column(String, primary_key=True)
    user_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(datetime.UTC))
    updated_at = Column(DateTime, default=datetime.now(datetime.UTC), onupdate=datetime.now(datetime.UTC))
    finished_at = Column(DateTime)
    status = Column(Enum(StatusConversationEnum), default=StatusConversationEnum.START, nullable=False)
    messages = relationship("MessagesSchema", back_populates="conversation")
    