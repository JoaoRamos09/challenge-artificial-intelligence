from typing import TypedDict
from langchain_core.messages import BaseMessage
from app.backend.dto.extract_data_dto import ExtractDataDTO

class ChatAIState(TypedDict):
    safety: bool
    insufficent_information: bool
    messages: list[BaseMessage]
    extract_data: ExtractDataDTO