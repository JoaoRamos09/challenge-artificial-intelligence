from pydantic import BaseModel, Field
from typing import Literal

class PreferencesUserDTO(BaseModel):
    level_technical: str = Field(..., description="Nível técnico do usuário, junior, mid, senior")
    preference_content: Literal["text", "video", "image"] = Field(..., description="Preferência de conteúdo do usuário, text, video, image")
    description: str = Field(..., description="Uma descrição detalhada do usuário, sua experiência, habilidades e interesses")
    weaknesses: str = Field(..., description="Os pontos técnicos que o usuário acha mais difíceis ou que precisa melhorar")
    strengths: str = Field(..., description="Os pontos que o usuário se orgulha e que acredita que são seus pontos fortes")
