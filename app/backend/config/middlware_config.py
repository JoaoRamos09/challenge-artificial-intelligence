from fastapi import Request
import time
import logging

async def request_middleware(request: Request, call_next):
    start_time = time.time()
    logging.info(f"[REQUEST] {request.method} {request.url.path}")
    response = await call_next(request)
    process_time = time.time() - start_time
    logging.info(f"[RESPONSE] {request.method} {request.url.path} - {response.status_code} ({process_time:.2f}s)")
    return response