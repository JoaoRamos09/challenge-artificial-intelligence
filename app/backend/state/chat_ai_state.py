from typing import TypedDict
from langchain_core.messages import BaseMessage
from app.backend.dto.preferences_user_dto import PreferencesUserDTO

class ChatAIState(TypedDict):
    safety: bool
    question: str
    insufficent_information: bool
    messages: list[BaseMessage]
    preferences_user: PreferencesUserDTO