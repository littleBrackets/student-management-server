from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from .model import Item


def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, id: int):
    return db.query(Item).filter(Item.id == id).first()


def create_item(db: Session, id: int, title: str, description: str):
    db_item = Item(id=id, title=title, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  


def update_item(db: Session, id: int, title: str, description: str):
    db_item = db.query(Item).filter(Item.id == id).first()
    if db_item:
        db_item.title = title
        db_item.description = description
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def delete_item(db: Session, id: int):
    db_item = db.query(Item).filter(Item.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    else:
        return None
