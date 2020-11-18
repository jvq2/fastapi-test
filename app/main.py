from fastapi import FastAPI, Depends

from app.auth import requires_user
from app.config import APP_CONFIG
from app.utils.database import init_db_conn
from app.routers import root, items, users, ensure_indexes, token, pytest

init_db_conn(APP_CONFIG)

app = FastAPI()

app.include_router(root.router)
app.include_router(token.router)
app.include_router(items.router)
app.include_router(users.router, dependencies=[Depends(requires_user)])
app.include_router(pytest.router, prefix='/test')
app.include_router(ensure_indexes.router)
