from fastapi import  APIRouter
from app.users import route as userRoute

router = APIRouter()

router.include_router(
    userRoute.router,
    prefix="/users",
)

