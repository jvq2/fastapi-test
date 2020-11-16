from fastapi import APIRouter

from app.models import User


router = APIRouter()


@router.get("/ensure_indexes/")
def ensure_indexes():
    User.ensure_indexes()
    return {"success": True}
