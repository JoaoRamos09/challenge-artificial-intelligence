from app.backend.service.ai_service import AIService
from pathlib import Path
from langchain_core.messages import HumanMessage, SystemMessage
from app.backend.dto.video_analysis_dto import VideoAnalysisDTO
from app.backend.dto.chunk_dto import ChunkDTO
from app.backend.service.text_processing_service import TextProcessingService
from app.backend.service.file_service import FileService
from typing import List
import uuid
from app.backend.enum.type_file_enum import TypeFileEnum

class VideoProcessingService():
    def __init__(self, ai_service: AIService, text_processing_service: TextProcessingService, file_service: FileService):
        self.ai_service = ai_service
        self.text_processing_service = text_processing_service
        self.file_service = file_service
    
    def process_video(self,path:str):
        video_file = self.file_service.get_video_from_path(path)
        transcription = self.ai_service.invoke_whisper(video_file)
        chunks = self.transcription_to_chunks(transcription, path)

        return chunks
    
    def transcription_to_chunks(self,transcription:str, path:str):
        split_transcription = self.text_processing_service.split_text(transcription)
        chunks = []
        for chunk in split_transcription:
            analysis = self.get_analysis_video(chunk)
            chunk_dto = ChunkDTO(
                id=str(uuid.uuid4()), 
                content=chunk, 
                type_file=TypeFileEnum.VIDEO,
                path=path, 
                tags=analysis.tags, 
                metadata=self.format_metadata_dict(analysis.summary, analysis.subject, analysis.technical_level))
            chunks.append(chunk_dto)
        return chunks
    
    def format_metadata_dict(self, summary:str, subject:List[str], technical_level:str):
        return {
            "summary": summary if summary is not None else "",
            "subject": subject if subject is not None else [],
            "technical_level": technical_level if technical_level is not None else "easy"
        }
    
    def get_analysis_video(self,transcription:str):
        messages = [
            SystemMessage(content="""
                          Você é um especialista em análise de transcrições de vídeos.
                          Sua função é analisar a transcrição e fornecer um resumo, assunto e nível técnico.
                          
                          FORMATO EXATO:
                          {
                              "summary": "Resumo da transcrição",
                              "subject": "Assunto da transcrição",
                              "tags": "Palavras chaves da transcrição",
                              "technical_level": "Nível técnico da transcrição"
                          }
                          
                          REGRAS OBRIGATÓRIAS:
                          1. Responda APENAS o JSON, sem texto adicional
                          2. Inclua SEMPRE os três campos: "summary", "subject" e "technical_level"
                          3. "subject" deve ser uma lista de strings com os assuntos principais do vídeo (ex: ["tecnologia", "programacao"])
                          4. "tags" deve ser uma lista de strings com as palavras chaves do vídeo (ex: ["tecnologia", "programacao"])
                          5. "summary" deve ser um resumo do vídeo com no máximo 1000 caracteres
                          6. "technical_level" deve ser um nível técnico do vídeo (ex: "iniciante", "intermediário", "difícil")
                          7. Certifique-se de que o JSON está completo e válido
                          8. Não corte a resposta no meio
                          """),
            HumanMessage(content=transcription)
        ]
        
        return self.ai_service.invoke_llm(messages=messages, output_structured=VideoAnalysisDTO, provider="openai", model="gpt-4o-mini")
