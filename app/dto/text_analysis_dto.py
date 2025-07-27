from pydantic import BaseModel, Field
from typing import List, Literal

class TextAnalisysDTO(BaseModel):
    technical_level: Literal["iniciante", "intemediário", "difícil"] = Field(
        description="Nível técnico do texto: 'iniciante' (fácil), 'intemediário' (intermediário) ou 'difícil' (difícil)."
    )
    subject: List[str] = Field(
        description="Lista de palavras-chave que representam os principais tópicos ou assuntos do texto."
    )
    