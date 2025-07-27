from fastapi import APIRouter, Depends
from app.service.text_processing_service import TextProcessingService
from app.service.image_processing_service import ImageProcessingService
from app.service.video_processing_service import VideoProcessingService
from app.service.ai_service import AIService
from app.service.file_service import FileService
from app.service.indexing_service import IndexingService
processing_data_router = APIRouter(prefix="/data-processing", tags=["process-data"])

def get_ai_service():
    return AIService()

def get_file_service():
    return FileService()

def get_indexing_service():
    return IndexingService()

def get_text_processing_service(ai_service: AIService = Depends(get_ai_service), file_service: FileService = Depends(get_file_service)):
    return TextProcessingService(ai_service, file_service)

def get_image_processing_service(ai_service: AIService = Depends(get_ai_service), file_service: FileService = Depends(get_file_service)):
    return ImageProcessingService(ai_service, file_service)

def get_video_processing_service(ai_service: AIService = Depends(get_ai_service), text_processing_service: TextProcessingService = Depends(get_text_processing_service), file_service: FileService = Depends(get_file_service)):
    return VideoProcessingService(ai_service, text_processing_service, file_service)

@processing_data_router.post("/text")
def process_text(path: str, text_processing_service: TextProcessingService = Depends(get_text_processing_service), indexing_service: IndexingService = Depends(get_indexing_service)):
    text = text_processing_service.process_text(file_name=path)
    indexing_service.save_data(text)
    return text

@processing_data_router.post("/image")
def process_image(path:str, image_processing_service: ImageProcessingService = Depends(get_image_processing_service)):
    response = image_processing_service.process_image(path)
    return response

@processing_data_router.post("/video")
def process_video(path:str, video_processing_service: VideoProcessingService = Depends(get_video_processing_service)):
    response = video_processing_service.process_video(path)
    return response