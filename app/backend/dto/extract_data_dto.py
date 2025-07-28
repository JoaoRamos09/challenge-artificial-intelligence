from pydantic import BaseModel, Field

class ExtractDataDTO(BaseModel):
    level_technical: str = Field(..., description="Nível técnico do usuário, junio, mid, senior	")
    preference_content: str = Field(..., description="Preferência de conteúdo do usuário, text, video, image")
    description: str = Field(..., description="Descrição do usuário")
    weaknesses: str = Field(..., description="Fraquezas do usuário")
    strengths: str = Field(..., description="Pontos fortes do usuário")
    question: str = Field(..., description="Pergunta do usuário")
