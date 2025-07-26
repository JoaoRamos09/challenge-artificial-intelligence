from pydantic import BaseModel

class TextDTO(BaseModel):
    content: str
    path: str
    tags: list[str]
    metadata: dict
