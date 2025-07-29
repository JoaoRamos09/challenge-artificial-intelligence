from fastapi import FastAPI
from app.backend.controller.data_processing_controller import processing_data_router
from app.backend.config.handler_config import setup_exception_handlers
from app.backend.controller.chat_ai_controller import chat_router

def create_app():
    app = FastAPI()
    setup_exception_handlers(app)
    app.include_router(processing_data_router)
    app.include_router(chat_router)
    return app