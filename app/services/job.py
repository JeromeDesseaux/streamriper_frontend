from uuid import UUID
from fastapi import BackgroundTasks
from sqlmodel import Session
from ..models.job import Job
from ..schemas import JobCreate
from ..utils import execute_shell_command, update_job_logs, update_job_status


async def start_job(db: Session, uid: UUID) -> None:
    job = db.get(Job, uid)
    if job is None:
        return
    job.result = execute_shell_command(uid, "https://www.example.com", {"key": "value"})
    update_job_status(job)
    update_job_logs(job, uid)
    db.commit()


async def task_handler(job: JobCreate, background_tasks: BackgroundTasks, db: Session):
    new_task = Job(
        url=job.url,
        service=job.service,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    background_tasks.add_task(start_job, db, new_task.uid)
    return new_task


async def status_handler(uid: UUID, db: Session):
    job = db.get(Job, uid)
    return job
