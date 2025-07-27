from fastapi import FastAPI
from app.handler.global_handler import global_exception_handler, handle_validation_exception, handle_generic_exception
from app.exception.base_exception import BaseException
from pydantic import ValidationError

def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(BaseException, global_exception_handler)
    app.add_exception_handler(ValidationError, handle_validation_exception)
    app.add_exception_handler(Exception, handle_generic_exception)
