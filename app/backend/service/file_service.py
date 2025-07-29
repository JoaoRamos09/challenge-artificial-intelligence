import os
from pathlib import Path
from app.backend.exception.file_exception import FileNotFound, InvalidTypeFileError, InvalidSuffixFileError, FileException
import base64
import json
import logging
class FileService():
    def __init__(self):
        pass
    
    def valid_file(self, path:str, allowed_formats:list):
    
        file_path = Path(path)
            
        if not file_path.exists():
            raise FileNotFound(path)
        
        if not file_path.is_file():
            raise InvalidTypeFileError(path)
        
        if not file_path.suffix in allowed_formats:
            raise InvalidSuffixFileError(path, allowed_formats)
        
        return file_path
    
    def get_file_text_from_path(self, file_name: str):
        logging.info(f"[GET FILE TEXT FROM PATH] - {file_name}")
        valid_file = self.valid_file(file_name, [".txt"])
        try:
            with open(valid_file, "r") as file:
                return file.read()
        except Exception as e:
            raise FileException(message="Error in get file text from path", file_path=file_name)
    
    def get_file_image_from_path(self, path:str):
        logging.info(f"[GET FILE IMAGE FROM PATH] - {path}")
        valid_file = self.valid_file(path, [".jpg", ".jpeg", ".png"])
        try:
            with open(valid_file, "rb") as img_file:
                base64_image = base64.b64encode(img_file.read()).decode("utf-8")
                return base64_image   
        except Exception as e:
            raise FileException(message="Error in get file image from path", file_path=path)
    
    ##Whisper close the file after use
    def get_video_from_path(self, path:str):
        logging.info(f"[GET VIDEO FROM PATH] - {path}")
        valid_file = self.valid_file(path, [".mp4"])
        try:
            video_file = open(valid_file, "rb")
            return video_file
        except Exception as e:
            raise FileException(message="Error in get video from path", file_path=path)
    
    def get_pdf_from_path(self, path:str):
        logging.info(f"[GET PDF FROM PATH] - {path}")
        valid_file = self.valid_file(path, [".pdf"])
        return valid_file
    
    def get_file_json_from_path(self, path:str):
        logging.info(f"[GET FILE JSON FROM PATH] - {path}")
        valid_file = self.valid_file(path, [".json"])
        try:
            with open(valid_file, "r") as file:
                return json.load(file)
        except Exception as e:
            raise FileException(message="Error in get file json from path", file_path=path)
    
    