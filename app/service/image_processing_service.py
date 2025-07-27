from app.service.ai_service import AIService
from app.dto.chunk_dto import ChunkDTO
from app.dto.image_analysis_dto import ImageAnalysisDTO
from langchain_core.messages import HumanMessage, SystemMessage
from app.service.file_service import FileService
import uuid
from app.enum.type_file_enum import TypeFileEnum

class ImageProcessingService:
    def __init__(self, ai_service: AIService, file_service: FileService):
        self.ai_service = ai_service
        self.file_service = file_service
        pass
    
    def process_image(self,path:str):
        image_base_url = self.file_service.get_file_image_from_path(path)
        response = self.get_analysis_image(image_base_url)
        return [ChunkDTO(
            id=str(uuid.uuid4()),
            content=response.description, 
            path=path, 
            tags=response.tags, 
            type_file=TypeFileEnum.IMAGE,
            metadata=self.format_metadata_dict(
                texts = response.texts,
                colors = response.colors, 
                objects = response.objects,
                technical_level = response.technical_level
            )
        )]
    
    def format_metadata_dict(self, texts: str, colors: list, objects: list, technical_level: str):
        return {
            "texts": texts if texts is not None else "",
            "colors": colors if colors is not None else [],
            "objects": objects if objects is not None else [],
            "technical_level": technical_level if technical_level is not None else ""
        } 
    
    def get_analysis_image(self,base64_image):
        messages = [
            SystemMessage(
                content="""
                Analise a imagem fornecida e extraia as seguintes informações:
                 - Descrição detalhada do conteúdo da imagem
                 - Os textos que estão na imagem
                 - Tags relevantes (ex: tecnologia, natureza, pessoas, etc.)
                 - Cores principais identificadas
                 - Objetos ou elementos visuais presentes
                 - Nível técnico da imagem: 'iniciante' (fácil), 'intemediário' (intermediário) ou 'difícil' (difícil).
                 
            Responda sempre no formato JSON especificado.
            """
            ),
            HumanMessage(
                content=[{
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                 }
                ]
            )
        ]
        
        return self.ai_service.invoke_llm(messages,provider="openai", model="gpt-4o-mini", output_structured=ImageAnalysisDTO)
    
    
    