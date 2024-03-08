from fastapi import  APIRouter
from app.users import route as user_route

router = APIRouter()

router.include_router(
    user_route.router,
    prefix="/users",
)

