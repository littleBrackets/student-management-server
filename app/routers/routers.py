from fastapi import Depends, APIRouter
from app.routers.endpoints import items, users
from app.dependencies import get_query_token, get_token_header

router = APIRouter()

router.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_query_token)],
    # responses={404: {"description": "Not found"}},
)
router.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)