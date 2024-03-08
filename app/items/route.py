from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db_session
from .curd import get_items

app = FastAPI()
router = APIRouter()

@router.get("/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    items = get_items(db, skip=skip, limit=limit)
    return items