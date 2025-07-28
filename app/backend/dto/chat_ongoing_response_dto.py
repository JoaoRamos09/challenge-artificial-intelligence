from pydantic import BaseModel
from app.backend.dto.message_dto import MessageDTO

class ChatOngoingResponseDTO(BaseModel):
    messages: list[MessageDTO]
    conversation_id: int
