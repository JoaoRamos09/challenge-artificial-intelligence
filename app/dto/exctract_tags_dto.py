from pydantic import BaseModel, Field
from typing import List, Literal

class ExtractTagsDTO(BaseModel):
    technical_level: Literal["easy","intermediary","hard"] = Field(description="List of tags extracted from the text, must contain only valid tags: easy, intermediare, hard")
    subject: List[str] = Field(description="List of keywords to extract the principal topics of the text")
    