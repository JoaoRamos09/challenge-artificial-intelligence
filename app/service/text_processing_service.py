from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.dto.chunk_dto import ChunkDTO
from app.service.ai_service import AIService
from langchain_core.messages import HumanMessage, SystemMessage
from app.dto.text_analysis_dto import TextAnalisysDTO
from app.service.file_service import FileService
import uuid
from app.dto.chunk_dto import TypeFile
class TextProcessingService:
    def __init__(self, ai_service: AIService, file_service: FileService):
        self.ai_service = ai_service
        self.file_service = file_service
        pass

    def process_text(self, file_name: str):
        text = self.file_service.get_file_text_from_path(file_name)
        split_texts = self.split_text(text)
        chunks = self.texts_to_chunks(texts=split_texts,file_name=file_name)
        return chunks
    
    
    def split_text(self, text: str):
        text.split()
        splitter = RecursiveCharacterTextSplitter(chunk_size=450, chunk_overlap=50)
        return splitter.split_text(text)
    
    def texts_to_chunks(self, texts:list, file_name:str):
        chunks = []
        for text in texts:
            response = self.get_analysis_text(text)
            text_dto = ChunkDTO(
                id=str(uuid.uuid4()), 
                content=text, 
                path= file_name, 
                tags=response.subject, 
                metadata={"technical_level": response.technical_level},
                type_file=TypeFile.TEXT)
            chunks.append(text_dto)
            
        return chunks
    
    def get_analysis_text(self, text):
        messages = [
            SystemMessage(content="""
            Analise o texto fornecido e responda APENAS com um JSON válido e completo.

            FORMATO EXATO:
            {
                "subject": ["tag1", "tag2", "tag3"],
                "technical_level": "easy"
            }

            REGRAS OBRIGATÓRIAS:
            1. Responda APENAS o JSON, sem texto adicional
            2. Inclua SEMPRE os dois campos: "subject" e "technical_level"
            3. "subject" deve ser uma lista de strings (ex: ["tecnologia", "programacao"])
            4. "technical_level" deve ser: "easy", "intermediary" ou "hard"
            5. Certifique-se de que o JSON está completo e válido
            6. Não corte a resposta no meio

            Exemplo de resposta válida:
            {
                "subject": ["tecnologia", "programacao", "web"],
                "technical_level": "intermediary"
            }
            """),
            HumanMessage(content=text)
        ]
        
        return self.ai_service.invoke_llm(messages=messages,output_structured=TextAnalisysDTO, provider="openai", model="gpt-4o-mini")
    
    
    
    
    
