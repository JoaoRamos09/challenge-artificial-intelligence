from typing import Optional
from fastapi import status
from app.backend.exception.base_exception import BaseException

class ConversationException(BaseException):
    
    def __init__(self, 
                 message: str,  
                 error_code: str = "CONVERSATION_ERROR",
                 status_code: int = status.HTTP_400_BAD_REQUEST,
                 id: Optional[int] = None,
                 service: Optional[str] = "CONVERSATION"
        ):
        details = {
            "id": id
        }
        super().__init__(
            message, 
            status_code=status_code, 
            error_code=error_code,
            details=details,
            service=service
        )

class ConversationAlreadyFinishedError(ConversationException):
    
    def __init__(self, id: int):
        super().__init__(
            message=f"Conversation already finished",
            id=id,
            error_code="CONVERSATION_ALREADY_FINISHED",
        )
class ConversationNotStartedError(ConversationException):
    
    def __init__(self,id: int):
        super().__init__(
            message=f"Conversation not started, user already has an ongoing conversation",
            error_code="CONVERSATION_NOT_STARTED",
            id=id
        )
        