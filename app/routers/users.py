from fastapi import APIRouter

from app.auth import hash_password
from app.exceptions import NotFound
from app.models import User
from app.utils.database import render_document
from app.views import UserView, UserCreate, UserUpdate

router = APIRouter()


@router.get("/users/")
async def list_users(limit: int = 1000, offset: int = 0):
    """Returns a list of users
    """
    # mongoengine does not support asyncio. Switching to motorengine will fix this
    query = User.objects.limit(limit).skip(offset)

    output = []
    for user in query.all():
        output.append(render_document(user, UserView))

    return output


@router.post("/users/")
async def create_user(user: UserCreate):
    """Create a new user
    """
    data = user.dict()

    if 'password' in data:
        data['password_hash'] = hash_password(data['password'])
        del data['password']

    new_user = User(**data).save()

    return render_document(new_user, UserView, exclude={'password_hash'})


@router.put("/users/{_user_id}")
async def update_user(_user_id: str, user: UserUpdate):
    """Update an existing user
    """
    query = User.objects(id=_user_id).limit(1)

    if not query.count():
        raise NotFound()

    modified_count = query.update_one(**user.dict())
    return {
        "modified": modified_count,
        "item": render_document(query[0], UserView, exclude={'password_hash'})
        # TODO: Sanitize the user data of the password hash
    }


@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    """Delete an existing user
    """
    user: User = User.by_id(user_id)

    user.delete()

    return {
        "deleted": 1
    }
