from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from .model import Item


def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Item).offset(skip).limit(limit).all()
