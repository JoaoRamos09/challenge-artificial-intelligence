from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.dto.text_dto import TextDTO

class TextProcessingService:
    def __init__(self):
        pass

    def process_text(self, file_name: str):
        try:
            text = self.get_text_from_path(file_name)
            chunks = self.split_text(text)
            texts_dto = [TextDTO(content=chunk, path=file_name, tags=[], metadata={}) for chunk in chunks]
            ##TODO: Extract tags and metadata from service AI
            return texts_dto
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
    
    
    
    
    
