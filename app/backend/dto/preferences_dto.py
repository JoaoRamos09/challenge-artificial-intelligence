from pydantic import BaseModel
from typing import Literal

class PreferenceDTO(BaseModel):
    level_technical: Literal["JUNIOR", "MID_LEVEL", "SENIOR"]
    preference_content: Literal["TEXT", "VIDEO", "IMAGE"]
    description: str
    weaknesses: str
    strengths: str

