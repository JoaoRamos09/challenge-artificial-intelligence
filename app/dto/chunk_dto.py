from pydantic import BaseModel
from app.enum.type_file_enum import TypeFileEnum
    
class ChunkDTO(BaseModel):
    id: str
    content: str
    path: str
    tags: list[str]
    metadata: dict
    type_file: TypeFileEnum
