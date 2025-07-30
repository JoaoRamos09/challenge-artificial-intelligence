from fastapi import Request
from fastapi.responses import JSONResponse
from app.backend.exception.base_api_exception import BaseAPIException
from pydantic import ValidationError
import logging

async def global_exception_handler(request: Request, exc: BaseAPIException):
    logging.error(f"[{exc.service}] - {exc.error_code}:{exc.detail}")
    return JSONResponse(
        status_code=exc.status_code, 
        content={
            "message": exc.detail, 
            "details": exc.details})

async def handle_validation_exception(request: Request, exc: ValidationError):
    logging.error(f"[VALIDATION ERROR] - {exc}")
    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation error",
            "details": {"validation_errors": exc.errors()}
        }
    )

async def handle_generic_exception(request: Request, exc: Exception):
    logging.error(f"[UNEXPECTED ERROR] - {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal server error",
            "details": {}
        }
    )