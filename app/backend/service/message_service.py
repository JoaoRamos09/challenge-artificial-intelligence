from app.backend.repository.message_repository import MessageRepository
from app.backend.schema.message_schema import MessageSchema
from app.backend.exception.default_exception import NotFoundError
from app.backend.mapper.message_mapper import MessageMapper

class MessageService():
    def __init__(self, message_repository: MessageRepository, message_mapper: MessageMapper):
        self.message_repository = message_repository
        self.message_mapper = message_mapper

    def get_message_by_id(self, message_id: int) -> MessageSchema:
        return self.message_repository.get_message_by_id(message_id)
    
    def save_messages(self, messages: list[MessageSchema]) -> list[MessageSchema]:
        return self.message_repository.create_messages(messages)
    
    def get_messages_by_conversation_id(self, conversation_id: int) -> list[MessageSchema]:
        messages = self.message_repository.get_messages_by_conversation_id(conversation_id)
        if not messages:
            raise NotFoundError(entity="Message", identifier=conversation_id)
        return messages
    

