from fastapi import  APIRouter
from app.users.route import router as userRouter
from app.items.route import router as itemRouter

router = APIRouter()

router.include_router(userRouter,prefix="/users")
router.include_router(itemRouter,prefix="/items")