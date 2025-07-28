from fastapi import Request
from fastapi.responses import JSONResponse
from app.backend.exception.base_exception import BaseException
from pydantic import ValidationError

async def global_exception_handler(request: Request, exc: BaseException):
    return JSONResponse(
        status_code=exc.status_code, 
        content={
            "message": exc.detail, 
            "details": exc.details})

async def handle_validation_exception(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation error",
            "details": {"validation_errors": exc.errors()}
        }
    )

async def handle_generic_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal server error",
            "details": {}
        }
    )