from pydantic import BaseModel
from enum import Enum

class TypeFile(Enum):
    IMAGE = "image"
    TEXT = "text"
    VIDEO = "video"
    PDF = "pdf"
    
class ChunkDTO(BaseModel):
    id: str
    content: str
    path: str
    tags: list[str]
    metadata: dict
    type_file: TypeFile
