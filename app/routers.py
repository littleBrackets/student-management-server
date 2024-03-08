from fastapi import  APIRouter
from app.users import route as userRoute
from app.items import route as itemRoute

router = APIRouter()

router.include_router(
    userRoute.router,
    prefix="/users",
)

router.include_router(
    itemRoute.router,
    prefix="/items",
)

