from fastapi import APIRouter

from app.views import ItemView


router = APIRouter()


# The q variable below was left in to demonstrate that prospector was working
@router.get("/items/{item_id}")
async def read_item(item_id: int, query: str = None):
    """Example GET endpoint that replays the sent data
    """
    return {"item_id": item_id, "query": query}


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemView):
    """Example PUT endpoint that replays a portion of the sent data
    """
    return {"item_name": item.name, "item_id": item_id}
