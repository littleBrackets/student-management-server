from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from .model import Subject, ReqSubjectModel, ResSubjectModel


def get_subject_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Subject).offset(skip).limit(limit).all()


def get_subject_by_id(db: Session, id: int):
    return db.query(Subject).filter(Subject.id == id).first()


def create_subject(db: Session,  form_data: ReqSubjectModel):
    db_item = Subject(name=form_data.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  


def update_subject(db: Session, form_data: ResSubjectModel):
    db_item = db.query(Subject).filter(Subject.id == form_data.id).first()
    if db_item:
        db_item.name = form_data.name
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def delete_subject(db: Session, id: int):
    db_item = db.query(Subject).filter(Subject.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    else:
        return None
