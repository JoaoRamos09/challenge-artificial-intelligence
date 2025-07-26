from pydantic import BaseModel

class ChunkDTO(BaseModel):
    content: str
    path: str
    technical_level: str
    tags: list[str]
    metadata: dict
