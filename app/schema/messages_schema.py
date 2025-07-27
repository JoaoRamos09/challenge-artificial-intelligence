from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from app.enum.type_message_enum import TypeMessageEnum

Base = declarative_base()

class MessagesSchema(Base):
    __tablename__ = "messages"
    
    id = Column(String, primary_key=True)
    conversation_id = Column(String, ForeignKey("conversations.id"))
    content = Column(Text, nullable=False)
    type_message = Column(Enum(TypeMessageEnum), nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.UTC))
