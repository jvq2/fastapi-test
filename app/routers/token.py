from datetime import datetime, timedelta
from random import randint

import jwt
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import requires_user, verify_password
from app.config import UNSECRET_KEY
from app.exceptions import NotFound, Unauthorized
from app.models import User
from app.utils.timing import normalize_timing
from app.views.token import TokenResponse

router = APIRouter()


def create_token(data: dict, expires_delta=timedelta(days=1)):
    """Creates a new JWT with the given data

    :param dict data: Data to encode into the token
    :param timedelta expires_delta: The expiration time of the token
    :returns bytes:
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + expires_delta

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, UNSECRET_KEY, algorithm="HS256")
    return encoded_jwt


async def auth_user(email: str, password: str):
    """Given an email and password, looks up a matching user in the db and
    validates their password. Returns the user on match or False if the email
    doesn't exist in the system or the password doesnt match.

    :param str email: The users email address
    :param str password: The password the user is attempting to login with
    :returns User|False:
    """
    try:
        user: User = User.by_email(email)
    except NotFound:
        return False

    if not verify_password(password, user.password_hash):
        return False

    return user


@router.post("/token", response_model=TokenResponse)
async def create_user_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Primary login endpoint for the application
    """
    # Ensure that the login request takes a standard amount of time whether
    # password matching is done or not.
    async with normalize_timing(randint(300, 500) / 1000):
        user = await auth_user(form_data.username, form_data.password)

    if not user:
        raise Unauthorized()

    access_token = create_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token/test", dependencies=[Depends(requires_user)])
async def test_token():
    """NOOP endpoint for testing that the user is authenticated
    """
    return {"success": 1}
