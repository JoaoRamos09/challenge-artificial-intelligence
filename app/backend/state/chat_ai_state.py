from typing import TypedDict
from langchain_core.messages import BaseMessage
from app.backend.dto.preferences_user_dto import PreferencesUserDTO
from typing import List
from pydantic import Field
from typing import Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class ChatAIState(TypedDict):
    input_user: str = Field(
        default="",
        description="Entrada do usuário"
    )
    
    messages: Annotated[list[AnyMessage], add_messages]
    
    messages_user: Annotated[list[AnyMessage], add_messages]
    
    answer_ai: dict = Field(
        default={},
        description="Resposta da IA"
    )
    
    sufficient_information: bool = Field(
        default=True,
        description="Indica se as informações coletadas são suficientes para o usuário"
    )
    
    safety: bool = Field(
        default=True,
        description="Indica se a entrada do usuário passou por uma verificação de segurança. Se True, significa que o conteúdo foi considerado seguro para processamento; se False, pode conter informações sensíveis, inadequadas ou perigosas, e deve ser tratado com cautela ou bloqueado. Este campo é fundamental para garantir a integridade e a conformidade do sistema com políticas de uso responsável."
    )
    
    preferences_user: PreferencesUserDTO = Field(
        default=None,
        description="Preferências do usuário"
    )
    