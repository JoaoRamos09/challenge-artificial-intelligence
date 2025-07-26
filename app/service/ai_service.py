from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from app.dto.exctract_tags_dto import ExtractTagsDTO

default_model = "meta-llama/llama-4-maverick-17b-128e-instruct"

class AIService():
    def __init__(self) -> None:
        pass
    
    def invoke_llm(self,messages, output_structured=None):
            try:
                result = self.get_llm(output_structured).invoke(input=messages)
                return result
            ##TODO: Add custom exception
            except Exception as e:
                raise e
    
    def get_llm(self,output_structured:str, model:str = default_model):
        try:
            return ChatGroq(model=model).with_structured_output(output_structured)
        ##TODO: Add custom exception
        except Exception as e:
            raise
    
    def extract_tags_by_llm(self,text:str):
        messages = [
            SystemMessage(
                content=
                """
                Você é um extrator de palavras-chaves de textos voltados para a área de programaçaõ e tecnologia, você irá analisar um texto e coletar as seguintes informações dele:
                
                **Tags de Nível Técnico: Qual é o nível técnico necessário para entender o texto? ['easy','intermediare','hard']
                **Tags de Tópicos: Quais são os principais tópicos do text? Exemplo: 'html', 'introduction' 'python' 
                         """
            ),
            HumanMessage(
                content=
                f"""
                Análise o texto e extrai as tags:
                {text}
                """
            )
        ]
        return self.invoke_llm(messages=messages, output_structured=ExtractTagsDTO)
            
    
    