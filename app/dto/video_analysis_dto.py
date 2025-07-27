from pydantic import BaseModel, Field
from typing import List, Literal

class VideoAnalysisDTO(BaseModel):
    summary: str = Field(description="Resumo da transcrição")
    subject: List[str] = Field(description="Os assuntos principais da transcrição")
    tags: List[str] = Field(description="Uma lista com as principais palavras chave da transcrição")
    technical_level: Literal["iniciante", "intemediário", "difícil"] = Field(
        description="Nível técnico do texto: 'iniciante' (fácil), 'intemediário' (intermediário) ou 'difícil' (difícil)."
    )
