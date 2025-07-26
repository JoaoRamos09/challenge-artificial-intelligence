from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.dto.chunk_dto import ChunkDTO
from app.service.ai_service import AIService

class TextProcessingService:
    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service
        pass

    def process_text(self, file_name: str):
        try:
            text = self.get_text_from_path(file_name)
            split_texts = self.split_text(text)
            chunks = self.texts_to_chunks(texts=split_texts,file_name=file_name)
            return chunks
        except FileNotFoundError as e:
            raise e
        except Exception as e:
            raise e
        
    def get_text_from_path(self, file_name: str):
        file_path = Path(file_name)
        with open(file_path, "r") as file:
            return file.read()
    
    
    def split_text(self, text: str):
        text.split()
        splitter = RecursiveCharacterTextSplitter(chunk_size=450, chunk_overlap=50)
        return splitter.split_text(text)
    
    def texts_to_chunks(self, texts:list, file_name:str):
        chunks = []
        for text in texts:
            response = self.ai_service.extract_tags_by_llm(text)
            text_dto = ChunkDTO(content=text, path= file_name, technical_level=response.technical_level, tags=response.subject, metadata={})
            chunks.append(text_dto)
        return chunks
    
    
    
    
    
