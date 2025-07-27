from fastapi import APIRouter, Depends
from app.service.text_processing_service import TextProcessingService
from app.service.image_processing_service import ImageProcessingService
from app.service.video_processing_service import VideoProcessingService
from app.service.ai_service import AIService
from app.service.file_service import FileService
from app.service.indexing_service import IndexingService
from app.service.pdf_processing_service import PDFProcessingService
from app.dto.chunk_dto import ChunkDTO
from app.service.json_processing_service import JsonProcessingService


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

def get_pdf_processing_service(file_service: FileService = Depends(get_file_service), text_processing_service: TextProcessingService = Depends(get_text_processing_service), ai_service: AIService = Depends(get_ai_service)):
    return PDFProcessingService(file_service, text_processing_service, ai_service)

def get_json_processing_service(file_service: FileService = Depends(get_file_service), ai_service: AIService = Depends(get_ai_service)):
    return JsonProcessingService(file_service, ai_service)

@processing_data_router.post("/text", response_model=list[ChunkDTO])
def process_text(path: str, text_processing_service: TextProcessingService = Depends(get_text_processing_service), indexing_service: IndexingService = Depends(get_indexing_service)):
    text = text_processing_service.process_text(file_name=path)
    indexing_service.save_data(text)
    return text

@processing_data_router.post("/image", response_model=list[ChunkDTO])
def process_image(path:str, image_processing_service: ImageProcessingService = Depends(get_image_processing_service), indexing_service: IndexingService = Depends(get_indexing_service)):
    response = image_processing_service.process_image(path)
    indexing_service.save_data(response)
    return response

@processing_data_router.post("/video", response_model=list[ChunkDTO])
def process_video(path:str, video_processing_service: VideoProcessingService = Depends(get_video_processing_service), indexing_service: IndexingService = Depends(get_indexing_service)):
    response = video_processing_service.process_video(path)
    indexing_service.save_data(response)
    return response

@processing_data_router.post("/pdf", response_model=list[ChunkDTO])
def process_pdf(path:str, pdf_processing_service: PDFProcessingService = Depends(get_pdf_processing_service), indexing_service: IndexingService = Depends(get_indexing_service)):
    response = pdf_processing_service.process_pdf(path)
    indexing_service.save_data(response)
    return response

@processing_data_router.post("/json", response_model=list[ChunkDTO])
def process_json(path:str, json_processing_service: JsonProcessingService = Depends(get_json_processing_service), indexing_service: IndexingService = Depends(get_indexing_service)):
    response = json_processing_service.process_json(path)
    indexing_service.save_data(response)
    return response
