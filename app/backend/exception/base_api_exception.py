from fastapi import HTTPException, status
from typing import Optional, Dict, Any

class BaseAPIException(HTTPException):
    def __init__(self, message: str, status_code:int = status.HTTP_500_INTERNAL_SERVER_ERROR, error_code:Optional[str] = None, details: Optional[Dict[str, Any]] = None, service: Optional[str] = None):
        self.error_code = error_code or f"HTTP_{status_code}"
        self.details = details or {}
        self.service = service
        super().__init__(status_code=status_code, detail=message)
        
        
