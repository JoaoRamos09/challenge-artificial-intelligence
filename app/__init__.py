from fastapi import FastAPI
from app.backend.controller.data_processing_controller import processing_data_router
from app.backend.config.handler_config import setup_exception_handlers
from app.backend.controller.chat_controller import chat_router
import coloredlogs
import sys
from app.backend.config.middlware_config import request_middleware
from app.backend.controller.chat_ai_controller import chat_router

coloredlogs.install(level='INFO', fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', stream=sys.stdout, level_styles={
        'info': {'color': 'green'},
        'warning': {'color': 'yellow'},
        'error': {'color': 'red', 'bold': True},
        'critical': {'color': 'red', 'bold': True}
    })

def create_app():
    app = FastAPI()
    setup_exception_handlers(app)
    app.middleware("http")(request_middleware)
    app.include_router(processing_data_router)
    app.include_router(chat_router)
    return app