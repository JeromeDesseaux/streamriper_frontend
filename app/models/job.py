from enum import Enum
from typing import Optional
from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field, create_engine, Session, Enum as SQLEnum


class JobStatus(str, Enum):
    __slots__ = ()
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"
    FAILED = "failed"


class JobService(str, Enum):
    __slots__ = ()
    DEEZER = "deezer"
    SPOTIFY = "spotify"
    QOBUZ = "qobuz"


class Job(SQLModel, table=True):
    __slots__ = ()
    uid: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    url: str = Field(max_length=100)
    status: JobStatus = Field(
        default=JobStatus.IN_PROGRESS, sa_column=SQLEnum(JobStatus)
    )
    service: JobService = Field(
        default=JobService.DEEZER, sa_column=SQLEnum(JobService)
    )
    result: Optional[int] = None
    logs: Optional[str] = None


engine = create_engine("sqlite:///./jobs.db")
SessionLocal = Session(engine)


def get_db():
    with SessionLocal as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
