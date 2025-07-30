from app.backend.exception.base_api_exception import BaseAPIException
from typing import Optional
from fastapi import status

class PineconeException(BaseAPIException):
    
    def __init__(self, 
                 message: str, 
                 namespace: Optional[str] = None,
                 index: Optional[str] = None,
                 error_code: str = "PINECONE_ERROR",
                 status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
                 service: Optional[str] = "PINECONE"
        ):
        details = {"namespace": namespace, "index": index} if namespace and index else {}
        super().__init__(
            message, 
            status_code=status_code, 
            details=details,
            error_code=error_code,
            service=service
        )
        
        
class PineconeIndexNotFound(PineconeException):
    def __init__(self, index: str):
        super().__init__(
            message=f"Index not found",
            index=index,
            error_code="PINECONE_INDEX_NOT_FOUND",
        )

class PineconeUpsertError(PineconeException):
    def __init__(self, namespace: str, index: str):
        super().__init__(
            message=f"Error upserting data into Pinecone",
            namespace=namespace,
            index=index,
            error_code="PINECONE_UPSERT_ERROR",
        )

class PineconeRetrieveError(PineconeException):
    def __init__(self, namespace: str, index: str):
        super().__init__(
            message=f"Error retrieving data from Pinecone",
            namespace=namespace,
            index=index,
            error_code="PINECONE_RETRIEVE_ERROR",
        )