from fastapi import FastAPI
from .routes import job


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(job.router)
    return application
