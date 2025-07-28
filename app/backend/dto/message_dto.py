from pydantic import BaseModel
from app.backend.enum.type_content_enum import TypeContentEnum
from app.backend.enum.type_message_enum import TypeMessageEnum

class MessageDTO(BaseModel):
    content: str
    type_content: TypeContentEnum
    type_message: TypeMessageEnum
