from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.views.base import PydanticObjectId


class TestRunView(BaseModel):
    class Config:
        orm_mode = True

    # TODO: get openapi docs to render when using PydanticObjectId
    id: PydanticObjectId
    started: datetime
    return_code: Optional[int] = ...
    stdout: Optional[str] = ...


class TestRunCreate(BaseModel):
    class Config:
        orm_mode = True

    id: PydanticObjectId
    created: bool
