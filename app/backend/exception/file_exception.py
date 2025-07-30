from typing import Optional, Dict, Any
from fastapi import status
from app.backend.exception.base_api_exception import BaseAPIException


class FileException(BaseAPIException):
    
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

class InvalidTypeFileError(FileException):
    
    def __init__(self, file_path: str):
        super().__init__(
            message=f"Not a valid file",
            file_path=file_path,
            error_code="INVALID_TYPE_FILE_ERROR",
        )

class InvalidSuffixFileError(FileException):
    
    def __init__(self, file_path: str, expected_suffix: list[str]):
        super().__init__(
            message=f"Sufix not allowed: {', '.join(expected_suffix)}",
            file_path=file_path,
            error_code="INVALID_SUFFIX_FILE_ERROR",
        )
        
        
        