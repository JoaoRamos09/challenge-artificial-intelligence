from fastapi import FastAPI
from app.controller.data_processing_controller import processing_data_router

def create_app():
    app = FastAPI()
    app.include_router(processing_data_router)
    return app