from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from openai import OpenAI
import openai
from app.backend.exception.ai_exception import InvalidProviderError, InvokeModelError
import logging
import time
from pathlib import Path
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
            raise InvalidProviderError(model, provider, )

        if provider == "openai":
            if output_structured:
                return ChatOpenAI(model=model, temperature=0.1).with_structured_output(output_structured)
            return ChatOpenAI(model=model, temperature=0.1)
        
        elif provider == "groq":
            if output_structured:
                return ChatGroq(model=model, temperature=0.1).with_structured_output(output_structured)
            return ChatGroq(model=model, temperature=0.1) 
       
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
    
    def invoke_text_to_speech(self, text, filename: str = None):
        logging.info(f"[INVOKE TEXT TO SPEECH] - {text[:15]}...")
        try:
            client = OpenAI()
        
            audio_dir = Path("generated_audio")
            audio_dir.mkdir(exist_ok=True)
            
            if not filename:
                filename = f"speech_{int(time.time())}.mp3"
            
            speech_file_path = audio_dir / filename
            
            with client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts", 
                voice="alloy",
                input=text,
                response_format="mp3"
            ) as response:
                response.stream_to_file(speech_file_path)
            
            full_path = speech_file_path.absolute()
            logging.info(f"[INVOKING TEXT TO SPEECH] - Audio saved at: {full_path.name}")
            return str(full_path)
            
        except Exception as e:
            logging.error(f"[INVOKE TEXT TO SPEECH ERROR] - {str(e)}")
            raise InvokeModelError("gpt-4o-mini-tts", "openai")
    
    
    