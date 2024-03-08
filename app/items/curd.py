from sqlalchemy.orm import Session
from .model import Item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item_by_owner(db: Session, owner_id: int):
    return db.query(Item).filter(Item.owner_id == owner_id).all()