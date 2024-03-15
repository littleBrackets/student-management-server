from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from .model import Class, ReqClassModel, ResClassModel


def get_class_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Class).offset(skip).limit(limit).all()


def get_class_by_id(db: Session, id: int):
    return db.query(Class).filter(Class.id == id).first()


def create_class(db: Session,  form_data: ReqClassModel):
    db_item = Class(name=form_data.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  


def update_class(db: Session, form_data: ResClassModel):
    db_item = db.query(Class).filter(Class.id == form_data.id).first()
    if db_item:
        db_item.name = form_data.name
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def delete_class(db: Session, id: int):
    db_item = db.query(Class).filter(Class.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    else:
        return None
