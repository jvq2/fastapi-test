from fastapi import APIRouter

from app.models import User


router = APIRouter()


@router.get('/ensure_indexes/')
def ensure_indexes():
    """Runs mongoengine maintanance function to create any missing db indexes
    """
    # TODO: catch errors from ensure indexes
    User.ensure_indexes()
    # ensure_indexes has no output, always return true.
    return {'success': True}
