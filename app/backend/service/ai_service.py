from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from openai import OpenAI
from app.backend.exception.ai_exception import InvalidProviderError, InvokeModelError
import logging
import base64
import os

default_model = "meta-llama/llama-4-maverick-17b-128e-instruct"
default_provider = "groq"

class AIService():
    def __init__(self) -> None:
        pass
    
    def invoke_llm(self,messages,provider:str = default_provider, model:str = default_model,output_structured=None):
        logging.info(f"[INVOKE LLM] - {provider}:{model} ")
        try:
            result = self.get_llm(provider,output_structured, model).invoke(input=messages)
            return result
        except(InvalidProviderError) as e:
            raise e
        except Exception as e:
            raise InvokeModelError(model, provider)
    
    def get_llm(self,provider:str, output_structured, model:str):
        
        if provider not in ["openai", "groq"]:
            raise InvalidProviderError(model, provider)

        if provider == "openai":
            if output_structured:
                return ChatOpenAI(model=model).with_structured_output(output_structured)
            return ChatOpenAI(model=model)
        
        elif provider == "groq":
            if output_structured:
                return ChatGroq(model=model).with_structured_output(output_structured)
            return ChatGroq(model=model) 
       
    def invoke_whisper(self,path_file):
        logging.info(f"[INVOKE WHISPER] - {path_file}")
        try:
            client = OpenAI()
            transcription = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe", 
            file=path_file, 
            response_format="text"
            )
            return transcription
        except Exception as e:
            
            raise InvokeModelError("whisper", "openai")
    
    def invoke_model_vision(self, prompt_user, user_id):
        logging.info(f"[INVOKE MODEL VISION] Invoking the model vision, user_id: {user_id}")
        try:
            client = OpenAI()      
            result = client.images.generate(
                model="gpt-image-1",
                prompt=prompt_user,
                size="1024x1024",
                quality="medium"
            )

            image_base64 = result.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            file_name = f"{user_id}.png"
            with open(file_name, "wb") as f:
                f.write(image_bytes)
            full_path = os.path.abspath(file_name)
            return full_path
        
        except Exception as e:
            raise InvokeModelError("vision", str(e))
    
    