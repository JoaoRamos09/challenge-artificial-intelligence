from fastapi import APIRouter, Depends
from app.backend.dto.chat_start_input_dto import ChatStartInputDTO
from app.backend.dto.chat_start_response_dto import ChatStartResponseDTO
from app.backend.schema.conversation_schema import ConversationSchema
from app.backend.enum.status_conversation_enum import StatusConversationEnum
from app.backend.schema.message_schema import MessageSchema
from app.backend.service.conversation_service import ConversationService
from app.backend.repository.conversation_repository import ConversationRepository
from app.backend.repository.message_repository import MessageRepository
from app.backend.service.message_service import MessageService
from app.backend.database.postgres import get_db
from app.backend.enum.type_content_enum import TypeContentEnum
from app.backend.enum.type_message_enum import TypeMessageEnum
from sqlalchemy.orm import Session
from app.backend.dto.chat_ongoing_input_dto import ChatOngoingInputDTO
from app.backend.dto.chat_ongoing_response_dto import ChatOngoingResponseDTO
from app.backend.mapper.message_mapper import MessageMapper
chat_router = APIRouter(prefix="/chat", tags=["chat"])

def get_conversation_repository(db: Session = Depends(get_db)):
    return ConversationRepository(db)

def get_message_repository(db: Session = Depends(get_db)):
    return MessageRepository(db)

def get_message_mapper():
    return MessageMapper()

def get_conversation_service(conversation_repository: ConversationRepository = Depends(get_conversation_repository)):
    return ConversationService(conversation_repository)    

def get_message_service(message_repository: MessageRepository = Depends(get_message_repository), message_mapper: MessageMapper = Depends(get_message_mapper)):
    return MessageService(message_repository, message_mapper)

@chat_router.post("/start", status_code=201, response_model=ChatStartResponseDTO)
def start_chat(chat_start_input_dto: ChatStartInputDTO, conversation_service: ConversationService = Depends(get_conversation_service), message_service: MessageService = Depends(get_message_service)):
    
    conversation = ConversationSchema(
        user_id=chat_start_input_dto.user_id,
        status=StatusConversationEnum.ONGOING
    )
    
    conversation_saved = conversation_service.start_conversation(conversation)

    messages = [
        MessageSchema(
            content=chat_start_input_dto.input_user,
            conversation_id=conversation_saved.id,
            type_content=TypeContentEnum.TEXT,
            type_message=TypeMessageEnum.HUMAN
        ),
        MessageSchema(
            content="Teste",
            conversation_id=conversation_saved.id,
            type_content=TypeContentEnum.TEXT,
            type_message=TypeMessageEnum.AI
        )
    ]
    
    messages_saved = message_service.save_messages(messages)
    
    return ChatStartResponseDTO(
        response=messages_saved[1].content,
        conversation_id=conversation_saved.id,
    )
    
@chat_router.post("/finished",status_code=204)
def finished_chat(conversation_id: int, conversation_service: ConversationService = Depends(get_conversation_service)):
    conversation_service.finished_conversation(conversation_id)
    return 

@chat_router.post("/ongoing", status_code=201, response_model=ChatOngoingResponseDTO)
def ongoing_chat(chat_ongoing_input_dto: ChatOngoingInputDTO, conversation_service: ConversationService = Depends(get_conversation_service), message_service: MessageService = Depends(get_message_service)):
    
    conversation = conversation_service.get_conversation_ongoing_by_id(chat_ongoing_input_dto.conversation_id)
    messages = message_service.get_messages_by_conversation_id(conversation.id)
    messages.append(MessageSchema(
        content=chat_ongoing_input_dto.input_user,
        conversation_id=conversation.id,
        type_content=TypeContentEnum.TEXT,
        type_message=TypeMessageEnum.HUMAN
    ))
    
    ##TODO: Call the AI to get the response
    ##TODO: Add preferences user
    
    messages_saved = message_service.save_messages(messages)
    
    return ChatOngoingResponseDTO(
        messages=message_service.message_mapper.to_dtos(messages_saved),
        conversation_id=conversation.id
    )
    
    
