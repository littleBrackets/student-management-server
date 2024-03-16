from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.dependencies import get_db_session
from .model import Institute, ReqInstituteModel, ReqUpdateInstituteModel

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


def get_institute_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Institute).offset(skip).limit(limit).all()


def get_institute_by_id(db: Session, id: int):
    return db.query(Institute).filter(Institute.id == id).first()


def create_institute(db: Session,  form_data: ReqInstituteModel, username: str):
    db_item = Institute()
    db_item.name = form_data.name
    db_item.address = form_data.address
    db_item.city = form_data.city
    db_item.state = form_data.state
    db_item.country = form_data.country
    db_item.pin_code = form_data.pin_code
    db_item.contact = form_data.contact
    db_item.email = form_data.email
    db_item.created_at = formatted_datetime
    db_item.updated_at = formatted_datetime
    db_item.created_by = username
    db_item.updated_by = username
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  


def update_institute(db: Session, form_data: ReqUpdateInstituteModel, username: str):
    db_item = db.query(Institute).filter(Institute.id == form_data.id).first()
    if db_item:
        db_item.name = form_data.name
        db_item.name = form_data.name
        db_item.address = form_data.address
        db_item.city = form_data.city
        db_item.state = form_data.state
        db_item.country = form_data.country
        db_item.pin_code = form_data.pin_code
        db_item.contact = form_data.contact
        db_item.email = form_data.email
        db_item.updated_at = formatted_datetime
        db_item.updated_by = username
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def delete_institute(db: Session, id: int):
    db_item = db.query(Institute).filter(Institute.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    else:
        return None
