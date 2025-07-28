from app.backend.schema.conversation_schema import ConversationSchema
from sqlalchemy.orm import Session
from typing import List
from app.backend.schema.message_schema import MessageSchema
from app.backend.enum.status_conversation_enum import StatusConversationEnum

class ConversationRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_conversation_by_id(self, conversation_id: int) -> ConversationSchema:
        return self.db.query(ConversationSchema).filter(ConversationSchema.id == conversation_id).first()

    def create_conversation(self, conversation: ConversationSchema) -> ConversationSchema:
        self.db.add(conversation)
        self.db.commit()
        return conversation
    
    def get_conversation_ongoing_by_id(self, conversation_id: int) -> ConversationSchema:
        return self.db.query(ConversationSchema).filter(ConversationSchema.id == conversation_id, ConversationSchema.status == StatusConversationEnum.ONGOING).first()
    
    def existis_ongoing_conversation(self, user_id: int) -> bool:
        return self.db.query(ConversationSchema).filter(ConversationSchema.user_id == user_id, ConversationSchema.status == StatusConversationEnum.ONGOING).first() is not None
