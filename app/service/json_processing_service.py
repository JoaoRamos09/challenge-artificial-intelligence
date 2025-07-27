from app.service.file_service import FileService
from app.dto.chunk_dto import ChunkDTO, TypeFile
from app.service.ai_service import AIService
import re
from langchain_core.messages import SystemMessage, HumanMessage
from app.dto.json_analysis_dto import JSONAnalysisDTO
import uuid

class JsonProcessingService:
    def __init__(self, file_service: FileService, ai_service: AIService):
        self.file_service = file_service
        self.ai_service = ai_service

    def process_json(self, path: str):
        json_data = self.file_service.get_file_json_from_path(path)
        chunks = []
        exercise_info = self.exctract_tags_exercise(json_data)
        
        if "content" in json_data:
            for question in json_data["content"]:
                chunk = self.create_chunk_by_question(question, exercise_info, path)
                chunks.append(chunk)
        
        return chunks
    
    def create_chunk_by_question(self, question:dict, exercise_info:dict, path:str):
        question_text = self.remove_html_tags(question["content"]["html"])
        options_text = self.extract_options_text(question["content"]["options"])
        full_content = f"""
        Questão: {question_text}

        Opções:
        {options_text}

        Resposta correta: {self.get_correct_answer(question["content"]["options"])}""".strip()
        analysis = self.get_analysis_json(full_content)
        
        return ChunkDTO(
            id=str(uuid.uuid4()),
            content=full_content,
            path=path,
            tags=analysis.tags,
            metadata=self.format_metadata_dict(analysis, question, exercise_info),
            type_file=TypeFile.TEXT
        )
    
    def get_analysis_json(self, question:str):
        messages = [
            SystemMessage(
                content="""
                Análise a questão e suas respostas fornecidas e extraia as seguintes informações:
                 - Faça um resumo da questão e respostas
                 - Tags relevantes (ex: tecnologia, natureza, pessoas, etc.)
                 - Assunto da questão
                 - Nível técnico da questão: 'iniciante' (fácil), 'intemediário' (intermediário) ou 'difícil' (difícil).
            
            Responda sempre no formato JSON especificado.
            """
            ),
            HumanMessage(
                content=question)
        ]
        
        return self.ai_service.invoke_llm(messages, provider="openai", model="gpt-4o-mini", output_structured=JSONAnalysisDTO)
    
    def exctract_tags_exercise(self,json_data:dict):
        return {
            "id": json_data.get("id", ""),
            "name": json_data.get("name", ""),
            "title": json_data.get("title", ""),
            "type": json_data.get("type", ""),
            "language": json_data.get("language", ""),
            "author": json_data.get("author", {}).get("name", ""),
            "category": json_data.get("category", ""),
            "tags": [tag.get("name", "") for tag in json_data.get("tags", [])]
        }
        
    def extract_options_text(self, options:list):
        options_text = []
        for i, option in enumerate(options, 1):
            option_text = self.remove_html_tags(option["content"]["html"])
            is_correct = "CORRETA" if option.get("correct", False) else "ERRADA"
            options_text.append(f"{i}. {option_text} {is_correct}")
        
        return "\n".join(options_text)
    
    def get_correct_answer(self, options:list):
        for i, option in enumerate(options, 1):
            if option.get("correct", False):
                return f"Opção {i}"
        return "Não especificada"
    
    def remove_html_tags(self, html_content:str):
        return re.sub(r'<[^>]*>', '', html_content)
    
    def format_metadata_dict(self, analysis:JSONAnalysisDTO, question:dict, exercise_info:dict):
        return {
            "question_id": question.get("external_questionId", ""),
            "position": question.get("position", 0),
            "exercise_name": exercise_info.get("name", ""),
            "exercise_title": exercise_info.get("title", ""),
            "exercise_type": exercise_info.get("type", ""),
            "author": exercise_info.get("author", {}),
            "category": exercise_info.get("category", ""),
            "language": exercise_info.get("language", ""),
            "question_title": question.get("title", ""),
            "summary": analysis.summary,
            "tags_question": analysis.tags,
            "subject": analysis.subject,
            "technical_level": analysis.technical_level
        }
    