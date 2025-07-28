from app.backend.schema.message_schema import MessageSchema
from app.backend.dto.message_dto import MessageDTO

class MessageMapper:
    def __init__(self):
        pass

    def to_dtos(self, messages: list[MessageSchema]) -> list[MessageDTO]:
        return [MessageDTO(
            content=message.content,
            type_content=message.type_content,
            type_message=message.type_message
        ) for message in messages]
