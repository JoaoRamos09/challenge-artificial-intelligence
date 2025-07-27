from app.service.ai_service import AIService
from pathlib import Path
from app.dto.chunk_dto import ChunkDTO
from app.dto.image_analysis_dto import ImageAnalysisDTO
from langchain_core.messages import HumanMessage, SystemMessage
import base64

class ImageProcessingService:
    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service
        pass
    
    def process_image(self,path:str):
        self.file_exists(path)
        image_base_url = self.encode_image(path=path)
        response = self.get_analysis_image(image_base_url)
        return ChunkDTO(content=response.description, 
                        path=path, technical_level="",
                        tags=response.tags, 
                        metadata=self.format_metadata_dict(
            texts = response.texts,
            colors = response.colors, 
            objects = response.objects))
    
    def encode_image(self, path:str):
        try:
            with open(path, "rb") as img_file:
                base64_image = base64.b64encode(img_file.read()).decode("utf-8")
                return base64_image
        ##TODO: Add custom exception    
        except Exception as e:
            raise Exception(f"Erro ao codificar a imagem em base64: {e}")
    
    def format_metadata_dict(self, texts: str, colors: list, objects: list):
        return {
            "texts": texts if texts is not None else "",
            "colors": colors if colors is not None else [],
            "objects": objects if objects is not None else []
        }
        
    ##TODO: Add service file
    def file_exists(self, path:str):
        file_path = Path(path)
        
        if not file_path.exists():
            raise FileNotFoundError
        
        if not file_path.is_file():
            raise ValueError   
    
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
    
    
    