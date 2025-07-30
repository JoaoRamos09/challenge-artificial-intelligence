from pydantic import BaseModel
from app.backend.dto.preferences_user_dto import PreferencesUserDTO
from typing import Optional
class ChatOngoingResponseDTO(BaseModel):
    
    answer_ai: str
    preferences_user: Optional[PreferencesUserDTO]