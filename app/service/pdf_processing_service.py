from PyPDF2 import PdfReader
from PyPDF2._page import PageObject
from app.service.file_service import FileService
from app.service.ai_service import AIService
from app.service.text_processing_service import TextProcessingService
from app.dto.chunk_dto import ChunkDTO, TypeFile
from langchain_core.messages import SystemMessage, HumanMessage
from app.dto.pdf_analysis_dto import PDFAnalysisDTO
import uuid

class PDFProcessingService:
    def __init__(self, file_service: FileService, text_processing_service: TextProcessingService, ai_service: AIService):
        self.file_service = file_service
        self.text_processing_service = text_processing_service
        self.ai_service = ai_service

    ##TODO: Add custom exception
    def process_pdf(self, path: str):
        file_path = self.file_service.get_pdf_from_path(path)
        pdf = self.read_pdf(file_path)
        return self.pdf_to_chunks(pdf, path)
    
    def pdf_to_chunks(self, pdf:PdfReader, path:str):
        chunks = []
        for page_number, page in enumerate(pdf.pages, start=1):
            texts = self.text_processing_service.split_text(page.extract_text(), chunk_size=700, chunk_overlap=100)
            # Extract analysis per page to avoid overprocessing all chunks
            analysis = self.get_analysis_pdf(page.extract_text())
            for text in texts:
                chunk_dto = ChunkDTO(
                    id=str(uuid.uuid4()),
                    content=text,
                    path=path,
                    tags=analysis.tags,
                    metadata=self.format_metadata_dict(analysis, pdf.metadata["/Title"], page_number),
                    type_file=TypeFile.PDF
                )
                chunks.append(chunk_dto)
        return chunks
    
    def format_metadata_dict(self, analysis:PDFAnalysisDTO, title:str, page:int):
        return {
            "subject": analysis.subject,
            "technical_level": analysis.technical_level,
            "title": title,
            "page": page
        }
                
    def read_pdf(self,path):
        try:
            return PdfReader(path)
        except Exception as e:
            raise 
    
    def get_analysis_pdf(self,text):
        messages = [
            SystemMessage(
                content="""
                Análise o trecho do PDF fornecido e extraia as seguintes informações:
                 - Descrição detalhada do conteúdo do trecho
                 - Tags relevantes (ex: tecnologia, natureza, pessoas, etc.
                 - Assunto do trecho
                 - Nível técnico do trecho: 'iniciante' (fácil), 'intemediário' (intermediário) ou 'difícil' (difícil).
            
            Responda sempre no formato JSON especificado.
            """
            ),
            HumanMessage(
                content=text
            )
        ]
        
        return self.ai_service.invoke_llm(messages,provider="openai", model="gpt-4o-mini", output_structured=PDFAnalysisDTO)
    
    
        
        

