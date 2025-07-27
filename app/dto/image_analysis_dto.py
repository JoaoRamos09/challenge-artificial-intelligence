from pydantic import BaseModel, Field
from typing import List

class ImageAnalysisDTO(BaseModel):
    description: str = Field(description="Descrição detalhada e abrangente do conteúdo visual da imagem, incluindo contexto, cenário e possíveis interpretações.")
    texts: str = Field(description="Todos os textos legíveis presentes na imagem, transcritos de forma fiel.")
    tags: List[str] = Field(description="Lista de palavras-chave ou categorias relevantes que representam os principais temas, assuntos ou elementos da imagem.")
    colors: List[str] = Field(description="Principais cores predominantes na imagem, descritas por nome ou código hexadecimal.")
    objects: List[str] = Field(description="Lista dos objetos, elementos visuais ou entidades reconhecíveis identificados na imagem.")