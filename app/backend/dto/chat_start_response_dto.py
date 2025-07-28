from pydantic import BaseModel

class ChatStartResponseDTO(BaseModel):
    response: str
    conversation_id: int
