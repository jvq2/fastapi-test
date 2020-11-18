from typing import Optional

from pydantic import BaseModel, EmailStr
from pydantic.fields import Field

from app.views.base import PydanticObjectId


class UserView(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    email: EmailStr
    first_name: str
    last_name: str
    tags: list

    class Config:
        # `orm_mode` doesnt work with mongoengines lists.
        # See https://github.com/samuelcolvin/pydantic/issues/1221
        # orm_mode = True
        pass


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    tags: Optional[list]


class UserUpdate(UserCreate):
    email: Optional[EmailStr]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
