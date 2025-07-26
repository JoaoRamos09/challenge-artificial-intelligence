from fastapi import APIRouter, Depends
from app.service.text_processing_service import TextProcessingService

processing_data_router = APIRouter(prefix="/data-processing", tags=["process-data"])

def get_indexing_service():
    return TextProcessingService()

@processing_data_router.post("/text")
def process_text(path: str, processing_text_service: TextProcessingService = Depends(get_indexing_service)):
    text = processing_text_service.process_text(file_name=path)
    return text