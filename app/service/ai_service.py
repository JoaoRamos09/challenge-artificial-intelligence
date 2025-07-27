from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from openai import OpenAI

default_model = "meta-llama/llama-4-maverick-17b-128e-instruct"
default_provider = "groq"

class AIService():
    def __init__(self) -> None:
        pass
    
    def invoke_llm(self,messages,provider:str = default_provider, model:str = default_model,output_structured=None):
            try:
                result = self.get_llm(provider,output_structured, model).invoke(input=messages)
                return result
            ##TODO: Add custom exception
            except Exception as e:
                raise e
    
    def get_llm(self,provider:str, output_structured, model:str):
        try:
            if provider == "openai":
                if output_structured:
                    return ChatOpenAI(model=model).with_structured_output(output_structured)
                return ChatOpenAI(model=model)
            
            else:
                if output_structured:
                    return ChatGroq(model=model).with_structured_output(output_structured)
                return ChatGroq(model=model)
        ##TODO: Add custom exception    
        except Exception as e:
            raise e
    
    def invoke_whisper(self,path_file):
        client = OpenAI()
        transcription = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe", 
        file=path_file, 
        response_format="text"
        )
        
        return transcription
    
    