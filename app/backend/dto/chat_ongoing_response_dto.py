from pydantic import BaseModel
from app.backend.dto.message_dto import MessageDTO

class ChatOngoingResponseDTO(BaseModel):
    message: MessageDTO
    user_id: int
