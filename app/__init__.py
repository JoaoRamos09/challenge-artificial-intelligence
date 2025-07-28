from fastapi import FastAPI
from app.backend.controller.data_processing_controller import processing_data_router
from app.backend.config.handler_config import setup_exception_handlers

def create_app():
    app = FastAPI()
    setup_exception_handlers(app)
    app.include_router(processing_data_router)
    return app