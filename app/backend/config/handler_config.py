from fastapi import FastAPI
from app.backend.handler.global_handler import global_exception_handler, handle_validation_exception, handle_generic_exception
from app.backend.exception.base_api_exception import BaseAPIException
from pydantic import ValidationError

def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(BaseAPIException, global_exception_handler)
    app.add_exception_handler(ValidationError, handle_validation_exception)
    app.add_exception_handler(Exception, handle_generic_exception)
