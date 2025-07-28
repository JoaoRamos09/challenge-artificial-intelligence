from typing import Optional
from fastapi import status
from app.backend.exception.base_exception import BaseException

class AIException(BaseException):
    
    def __init__(self, 
                 message: str,  
                 error_code: str = "AI_ERROR",
                 status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
                 provider: Optional[str] = None,
                 model: Optional[str] = None,
                 service: Optional[str] = "AI"
        ):
        details = {
            "provider": provider, 
            "model": model, 
        }
        super().__init__(
            message, 
            status_code=status_code, 
            error_code=error_code,
            details=details,
            service=service
        )

class InvalidProviderError(AIException):
    
    def __init__(self, provider: str, model: Optional[str] = None):
        super().__init__(
            message=f"Invalid provider",
            provider=provider,
            model = model,
            error_code="INVALID_PROVIDER",
        )

class InvokeModelError(AIException):
    
    def __init__(self, model: str, provider: str):
        super().__init__(
            message=f"Error invoking model",
            model=model,
            provider=provider,
            error_code="INVOKE_MODEL_ERROR",
        )
