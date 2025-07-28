from typing import TypedDict
from langchain_core.messages import BaseMessage
from app.backend.dto.preferences_dto import PreferenceDTO

class ChatAIState(TypedDict):
    safety: bool
    insufficent_information: bool
    messages: list[BaseMessage]
    preferences_user: PreferenceDTO
    