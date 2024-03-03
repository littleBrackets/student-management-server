from fastapi import Depends, APIRouter
from app.routers.endpoints import items, users

router = APIRouter()

router.include_router(
    users.router,
    prefix="/users",
)
router.include_router(
    items.router,
    prefix="/items",
)
