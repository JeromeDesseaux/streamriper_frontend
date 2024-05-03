from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .models import create_db_and_tables
from .routes import job_router


app = FastAPI()

app.include_router(job_router, tags=["job"])

app.mount("/logs", StaticFiles(directory="logs"), name="logs")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Streamripper API is running"}
