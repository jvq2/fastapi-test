from typing import Optional

# from bson.errors import InvalidId
from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr
from pydantic.fields import Field


# Could not get pydantic to work with this custom field class despite the docs.
# ref: https://pydantic-docs.helpmanual.io/usage/types/#custom-data-types
class PydanticObjectId():

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @staticmethod
    def validate(value):
        if not isinstance(value, ObjectId):
            raise TypeError('ObjectId required')
        return str(value)


class UserView(BaseModel):
    # id: ObjectId = Field(alias='_id')
    id: PydanticObjectId = Field(alias='_id')
    email: EmailStr
    first_name: str
    last_name: str
    tags: list

    class Config:
        # `orm_mode` doesnt work with mongoengines lists.
        # See https://github.com/samuelcolvin/pydantic/issues/1221
        # orm_mode = True
        # arbitrary_types_allowed = True
        # json_encoders = {
        #     # datetime: lambda dt: dt.isoformat(),
        #     # PydanticObjectId: lambda oid: str(oid),
        #     ObjectId: lambda oid: str(oid),
        # }
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
