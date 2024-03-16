from fastapi import  APIRouter
from app.users.route import router as userRouter
from app.classes.route import router as classesRouter
from app.sections.route import router as sectionsRouter
from app.subjects.route import router as subjectsRouter
from app.tests.route import router as testsRouter
from app.institutes.route import router as institutesRouter

router = APIRouter()

router.include_router(userRouter,prefix="/users")
router.include_router(classesRouter,prefix="/classes")
router.include_router(sectionsRouter,prefix="/sections")
router.include_router(subjectsRouter,prefix="/subjects")
router.include_router(testsRouter,prefix="/tests")
router.include_router(institutesRouter,prefix="/institutes")