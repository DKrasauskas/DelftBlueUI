import subprocess
import asyncio

def get_queue():
    result = subprocess.run(
        ["bash", "shell/check_job_status.sh", "check"],
        capture_output=True,
        text=True,
        check=True
    )
    return [x.split() for x in result.stdout.split("\n") if len(x) != 0]
