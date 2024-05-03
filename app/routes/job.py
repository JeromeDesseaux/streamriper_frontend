from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlmodel import Session

from ..models.job import get_db
from ..schemas import JobRead, JobCreate
from ..services.job import task_handler, status_handler

router = APIRouter()


@router.post("/job", response_model=JobRead)
async def create_job(
    job: JobCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
):
    return await task_handler(job, background_tasks=background_tasks, db=db)


@router.get("/job/{job_id}", response_model=JobRead)
async def get_job(job_id: UUID, db: Session = Depends(get_db)):
    return await status_handler(job_id, db=db)
