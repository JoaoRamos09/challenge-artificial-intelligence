from pydantic import BaseModel

class ChatOngoingInputDTO(BaseModel):
    input_user: str
    conversation_id: int
    