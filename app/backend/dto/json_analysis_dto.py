from pydantic import BaseModel, Field
from typing import Literal
class JSONAnalysisDTO(BaseModel):
    summary: str = Field(description="Faça um resumo da questão e respostas")
    tags: list[str] = Field(description="Tags relevantes (ex: tecnologia, natureza, pessoas, etc.")
    subject: str = Field(description="Assunto da questão")
    technical_level: Literal["iniciante", "intemediário", "difícil"] = Field(
        description="Nível técnico do texto: 'iniciante' (fácil), 'intemediário' (intermediário) ou 'difícil' (difícil)."
    )
    
    