import os
from uuid import UUID
from typing import Optional
from subprocess import check_output, CalledProcessError

from app.models import Job, JobStatus


def execute_shell_command(job_uuid: UUID, stream_url: str, options: Optional[dict]):
    with open(f"logs/{job_uuid}.txt", "w") as log:
        return_code: int = 0
        out: bytes = b""
        try:
            out = check_output(["ls", "-l"])
        except CalledProcessError as e:
            out = e.output
            return_code = e.returncode
        finally:
            log.write(out.decode())
            return return_code


def update_job_logs(job: Job, uid: UUID) -> None:
    log_path = f"logs/{uid}.txt"
    if os.path.isfile(log_path):
        job.logs = "//" + log_path


def update_job_status(job: Job) -> None:
    if job.result == 0:
        job.status = JobStatus.COMPLETE
    else:
        job.status = JobStatus.FAILED
