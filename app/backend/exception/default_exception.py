from typing import Optional
from fastapi import status
from app.backend.exception.base_exception import BaseException

class DefaultException(BaseException):
    
    def __init__(self, 
                 message: str,  
                 error_code: str = "DEFAULT_ERROR",
                 status_code: int = status.HTTP_400_BAD_REQUEST,
                 entity: Optional[str] = None,
                 identifier: Optional[str] = None,
                 service: Optional[str] = "DEFAULT"
        ):
        details = {
            "entity": entity, 
            "identifier": identifier
        }
        super().__init__(
            message, 
            status_code=status_code, 
            error_code=error_code,
            details=details,
            service=service
        )

class NotFoundError(DefaultException):
    
    def __init__(self, entity: str, identifier: Optional[str] = None):
        super().__init__(
            message=f"Entity not found",
            entity=entity,
            identifier=identifier,
            error_code="NOT_FOUND",
            status_code=status.HTTP_404_NOT_FOUND
        )
