from app.backend.dto.message_dto import MessageDTO
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from app.backend.enum.type_message_enum import TypeMessageEnum
from app.backend.enum.type_content_enum import TypeContentEnum

class MessageMapper:
    def __init__(self):
        pass

    def to_base_messages(self, messages: list[MessageDTO]) -> list[BaseMessage]:
        base_messages = []
        
        for message in messages:
            if message.type_message == TypeMessageEnum.HUMAN:
                base_messages.append(HumanMessage(content=message.content))
            elif message.type_message == TypeMessageEnum.AI:
                base_messages.append(AIMessage(content=message.content))
            elif message.type_message == TypeMessageEnum.SYSTEM:
                base_messages.append(SystemMessage(content=message.content))
            else:
                base_messages.append(HumanMessage(content=message.content))
        
        return base_messages

    def from_base_messages(self, base_messages: list[BaseMessage]) -> list[MessageDTO]:
        message_dtos = []
        
        for message in base_messages:
            if isinstance(message, HumanMessage):
                message_dtos.append(MessageDTO(
                    content=message.content,
                    type_content=TypeContentEnum.TEXT,  
                    type_message=TypeMessageEnum.HUMAN
                ))
            elif isinstance(message, AIMessage):
                message_dtos.append(MessageDTO(
                    content=message.content,
                    type_content=TypeContentEnum.TEXT,  
                    type_message=TypeMessageEnum.AI
                ))
            elif isinstance(message, SystemMessage):
                message_dtos.append(MessageDTO(
                    content=message.content,
                    type_content=TypeContentEnum.TEXT,  
                    type_message=TypeMessageEnum.SYSTEM
                ))
            else:
                message_dtos.append(MessageDTO(
                    content=message.content,
                    type_content=TypeContentEnum.TEXT,
                    type_message=TypeMessageEnum.HUMAN
                ))
        
        return message_dtos
