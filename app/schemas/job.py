# Your Pydantic models for job creation and reading go here

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from ..models.job import JobStatus, JobService


class JobCreate(BaseModel):
    url: str
    service: JobService


class JobRead(BaseModel):
    uid: UUID
    url: str
    status: JobStatus
    service: JobService
    result: Optional[int]
    logs: Optional[str]

    class Config:
        orm_mode = True
