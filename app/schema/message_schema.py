from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Enum
from datetime import datetime
from app.enum.type_message_enum import TypeMessageEnum
from app.enum.type_content_enum import TypeContentEnum
from app.database.base import Base

class MessageSchema(Base):
    __tablename__ = "messages"
    
    id = Column(String, primary_key=True)
    conversation_id = Column(String, ForeignKey("conversations.id"))
    content = Column(Text, nullable=False)
    type_content = Column(Enum(TypeContentEnum), nullable=False)
    type_message = Column(Enum(TypeMessageEnum), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
