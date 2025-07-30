from fastapi import APIRouter, Depends
from app.backend.dto.chat_ongoing_input_dto import ChatOngoingInputDTO
from app.backend.service.chat_ai_service import ChatAIService
from app.backend.service.ai_service import AIService
from app.backend.dto.chat_ongoing_response_dto import ChatOngoingResponseDTO
from app.backend.service.indexing_service import IndexingService
from typing import Annotated

chat_router = APIRouter(prefix="/chat-ai", tags=["chat"])

def get_ai_service():
    return AIService()

def get_indexing_service():
    return IndexingService()

def get_chat_ai_service(ai_service: Annotated[AIService, Depends(get_ai_service)], indexing_service: Annotated[IndexingService, Depends(get_indexing_service)]):
    return ChatAIService(ai_service, indexing_service)

ChatAIServiceDep = Annotated[ChatAIService, Depends(get_chat_ai_service)]

@chat_router.post("/ongoing", status_code=201, response_model=ChatOngoingResponseDTO)
def ongoing_chat(chat_ongoing_input_dto: ChatOngoingInputDTO, chat_ai_service: ChatAIServiceDep):
    response = chat_ai_service.invoke_graph_chat_ai(chat_ongoing_input_dto.user_id, chat_ongoing_input_dto.input_user)
    if response["preferences_user"]:
        return ChatOngoingResponseDTO(
            answer_ai=response["answer_ai"]["content"],
            preferences_user=response["preferences_user"]
        )
    return ChatOngoingResponseDTO(
        answer_ai=response["answer_ai"]["content"],
        preferences_user=None
    )
