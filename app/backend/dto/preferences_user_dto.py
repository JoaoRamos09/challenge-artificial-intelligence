from pydantic import BaseModel, Field
from typing import Optional

class PreferencesUserDTO(BaseModel):
    level_technical: Optional[str] = Field(
        default=None,
        description="Nível técnico do usuário, por exemplo: júnior, pleno, sênior"
    )
    
    description: Optional[str] = Field(
        default=None,
        description="Descrição do perfil do usuário"
    )
    
    weaknesses: Optional[str] = Field(
        default=None,
        description="Pontos fracos do usuário"
    )
    
    type_content: Optional[str] = Field(
        default=None,
        description="Qual é a maneira que o usuário gosta de estudar? Por vídeo? texto, audio?",
        examples=["texto", "video", "audio"],
        pattern="^(texto|video|audio)?$"
    )
