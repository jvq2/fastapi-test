import asyncio

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def read_root():
    """Root of the application that does nothing
    """
    proc = await asyncio.create_subprocess_exec(
        "echo", "World!",
        stdout=asyncio.subprocess.PIPE
    )
    stdout, _ = await proc.communicate()

    return {"Hello": stdout.strip()}
