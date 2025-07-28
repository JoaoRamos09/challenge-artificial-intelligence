from app.backend.schema.message_schema import MessageSchema
from sqlalchemy.orm import Session
from typing import List
class MessageRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_message_by_id(self, message_id: int) -> MessageSchema:
        return self.db.query(MessageSchema).filter(MessageSchema.id == message_id).first()
    
    def create_messages(self, messages: list[MessageSchema]) -> list[MessageSchema]:
        self.db.add_all(messages)
        self.db.commit()
        return messages
    
    def delete_messages_by_conversation_id(self, conversation_id: int) -> None:
        self.db.query(MessageSchema).filter(MessageSchema.conversation_id == conversation_id).delete()
        self.db.commit()

    def get_messages_by_conversation_id(self, conversation_id: int) -> list[MessageSchema]:
        return self.db.query(MessageSchema).filter(MessageSchema.conversation_id == conversation_id).all()
    
 