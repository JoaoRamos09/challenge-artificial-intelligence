from pydantic import BaseModel, Field
from typing import Literal

class PDFAnalysisDTO(BaseModel):
    tags: list[str] = Field(description="As principais palavras chaves do PDF")
    subject: str = Field(description="Assunto do PDF")
    technical_level: Literal["iniciante", "intemediário", "difícil"] = Field(
        description="Nível técnico do texto: 'iniciante' (fácil), 'intemediário' (intermediário) ou 'difícil' (difícil)."
    )