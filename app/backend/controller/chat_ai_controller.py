from fastapi import APIRouter, Depends
from app.backend.dto.chat_ongoing_input_dto import ChatOngoingInputDTO
from app.backend.dto.chat_ongoing_response_dto import ChatOngoingResponseDTO
from app.backend.service.chat_ai_service import ChatAIService
from app.backend.service.ai_service import AIService
from typing import Annotated
from app.backend.mapper.message_mapper import MessageMapper
from app.backend.dto.message_dto import MessageDTO
from app.backend.enum.type_content_enum import TypeContentEnum
from app.backend.enum.type_message_enum import TypeMessageEnum

chat_router = APIRouter(prefix="/chat-ai", tags=["chat"])

def get_ai_service():
    return AIService()

def get_chat_ai_service(ai_service: Annotated[AIService, Depends(get_ai_service)]):
    return ChatAIService(ai_service)

def get_message_mapper():
    return MessageMapper()

ChatAIServiceDep = Annotated[ChatAIService, Depends(get_chat_ai_service)]
MessageMapperDep = Annotated[MessageMapper, Depends(get_message_mapper)]

@chat_router.post("/ongoing", status_code=201, response_model=ChatOngoingResponseDTO)
def ongoing_chat(chat_ongoing_input_dto: ChatOngoingInputDTO, chat_ai_service: ChatAIServiceDep, message_mapper: MessageMapperDep):
    
    message_dto = MessageDTO(
        content=chat_ongoing_input_dto.input_user,
        type_content=TypeContentEnum.TEXT,
        type_message=TypeMessageEnum.HUMAN
    )
    messages = message_mapper.to_base_messages([message_dto])
    base_message = chat_ai_service.invoke_graph_chat_ai(chat_ongoing_input_dto.user_id, messages)
    message_dto = message_mapper.from_base_messages(base_message["messages"])

    return ChatOngoingResponseDTO(
        message=message_dto[-1],
        user_id=chat_ongoing_input_dto.user_id
    )
