from fastapi import  APIRouter
from app.users.route import router as userRouter
from app.classes.route import router as classesRouter
from app.items.route import router as itemRouter

router = APIRouter()

router.include_router(userRouter,prefix="/users")
router.include_router(classesRouter,prefix="/classes")
router.include_router(itemRouter,prefix="/items")