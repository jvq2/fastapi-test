import jwt
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.param_functions import Depends
from passlib.context import CryptContext

from app.config import UNSECRET_KEY
from app.exceptions import Unauthorized
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Generate a cryptographic hash from a the users password

    :param str password: The users plain text password
    :returns str:
    """
    # Im not doing any salt or pepper here for time's sake
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """Validates that the given password matches the users password

    :param str password: The users plain text password
    :param str password_hash: The stored password hash from the db
    :returns bool:
    """
    # Im not doing any salt or pepper here for time's sake
    return pwd_context.verify(password, password_hash)


def decode_token(token: str):
    """Decodes and verifies a jwt

    :param str token: The users token
    :returns dict:
    :raises app.exceptions.Unauthorized:
    """
    try:
        return jwt.decode(token, UNSECRET_KEY, verify=True, algorithms=["HS256"])
    except jwt.exceptions.DecodeError:
        print("bad decode")
        raise Unauthorized()


def requires_user(token: str = Depends(oauth2_scheme)):
    """Validates the the clients sent a valid jwt

    :param str token: The users token
    :returns User:
    :raises app.exceptions.Unauthorized:
    """
    payload = decode_token(token)
    user_id = payload.get('sub')

    if user_id is None:
        print("user_id is none")
        raise Unauthorized()

    try:
        return User.by_id(user_id)
    except IndexError:
        print("user not found")
        raise Unauthorized()
