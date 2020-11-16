import asyncio

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def read_root():
    proc = await asyncio.create_subprocess_exec(
        "echo", "World!",
        stdout=asyncio.subprocess.PIPE
    )
    stdout, _ = await proc.communicate()

    return {"Hello": stdout.strip()}


# @router.get("/foo")
# async def read_foo():
#     return {"Hello": "foo"}
