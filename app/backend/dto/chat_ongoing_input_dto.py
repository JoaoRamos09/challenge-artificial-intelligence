from pydantic import BaseModel


class ChatOngoingInputDTO(BaseModel):
    input_user: str
    user_id: int
    