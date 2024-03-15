from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from .model import Section, ReqSectionModel, ResSectionModel


def get_section_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Section).offset(skip).limit(limit).all()


def get_section_by_id(db: Session, id: int):
    return db.query(Section).filter(Section.id == id).first()


def create_section(db: Session,  form_data: ReqSectionModel):
    db_item = Section(name=form_data.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  


def update_section(db: Session, form_data: ResSectionModel):
    db_item = db.query(Section).filter(Section.id == form_data.id).first()
    if db_item:
        db_item.name = form_data.name
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def delete_section(db: Session, id: int):
    db_item = db.query(Section).filter(Section.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    else:
        return None
