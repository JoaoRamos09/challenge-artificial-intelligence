from pydantic import BaseModel

class ChatStartInputDTO(BaseModel):
    input_user: str
    user_id: int