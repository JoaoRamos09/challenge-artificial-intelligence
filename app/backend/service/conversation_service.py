from app.backend.repository.conversation_repository import ConversationRepository
from app.backend.schema.conversation_schema import ConversationSchema
from app.backend.enum.status_conversation_enum import StatusConversationEnum
from app.backend.exception.default_exception import NotFoundError
from app.backend.exception.conversation_exception import ConversationAlreadyFinishedError, ConversationNotStartedError

class ConversationService():
    def __init__(self, conversation_repository: ConversationRepository):
        self.conversation_repository = conversation_repository

    def get_conversation_by_id(self, conversation_id: int) -> ConversationSchema:
        conversation = self.conversation_repository.get_conversation_by_id(conversation_id)
        if not conversation:
            raise NotFoundError(entity="Conversation", identifier=conversation_id)
        return conversation
    
    def get_conversation_ongoing_by_id(self, conversation_id: int) -> ConversationSchema:
        conversation = self.conversation_repository.get_conversation_ongoing_by_id(conversation_id)
        if not conversation:
            raise NotFoundError(entity="Conversation", identifier=conversation_id)
        return conversation
    
    def save_conversation(self, conversation: ConversationSchema) -> ConversationSchema:
        return self.conversation_repository.create_conversation(conversation)
    
    def start_conversation(self, conversation: ConversationSchema) -> ConversationSchema:
        if self.existis_ongoing_conversation(conversation.user_id):
            raise ConversationNotStartedError()
        return self.save_conversation(conversation)
    
    def validate_finished_conversation(self, conversation_id: int):
        conversation = self.get_conversation_by_id(conversation_id)
        if conversation.status == StatusConversationEnum.FINISHED:
            raise ConversationAlreadyFinishedError(id=conversation_id)
    
    def finished_conversation(self, conversation_id: int):
        self.validate_finished_conversation(conversation_id)
        conversation = self.get_conversation_by_id(conversation_id)
        conversation.status = StatusConversationEnum.FINISHED
        self.save_conversation(conversation)
    
    def existis_ongoing_conversation(self, user_id: int) -> bool:
        return self.conversation_repository.existis_ongoing_conversation(user_id)
