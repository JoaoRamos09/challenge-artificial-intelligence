from pydantic import BaseModel, Field
from typing import List

class VideoAnalysisDTO(BaseModel):
    summary: str = Field(description="Resumo da transcrição")
    subject: List[str] = Field(description="Os assuntos principais da transcrição")
    tags: List[str] = Field(description="Uma lista com as principais palavras chave da transcrição")
