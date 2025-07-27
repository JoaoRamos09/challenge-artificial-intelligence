from typing import Optional, Dict, Any
from fastapi import status


class FileException(BaseException):
    
    def __init__(self, 
                 message: str, 
                 file_path: Optional[str] = None, 
                 error_code: str = "FILE_ERROR",
                 status_code: int = status.HTTP_400_BAD_REQUEST,
                 service: Optional[str] = "FILE"
        ):
        details = {"file_path": file_path} if file_path else {}
        super().__init__(
            message, 
            status_code=status_code, 
            details=details,
            error_code=error_code,
            service=service
        )

class FileNotFound(FileException):
    
    def __init__(self, file_path: str):
        super().__init__(
            message=f"File not found",
            file_path=file_path,
            error_code="FILE_NOT_FOUND",
            status_code=status.HTTP_404_NOT_FOUND
        )

class InvalidTypeError(FileException):
    
    def __init__(self, file_path: str, expected_type: str):
        super().__init__(
            message=f"Invalid type: expected {expected_type}",
            file_path=file_path,
            error_code="INVALID_TYPE_FILE_ERROR",
        )
        
        
        