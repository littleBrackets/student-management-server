from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.dependencies import get_db_session
from .model import Staff, ReqStaffModel, ReqUpdateStaffModel

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


def get_staff_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Staff).offset(skip).limit(limit).all()


def get_staff_by_id(db: Session, id: int):
    return db.query(Staff).filter(Staff.id == id).first()


def create_staff(db: Session,  form_data: ReqStaffModel, username: str):
    db_item = Staff()
    db_item.first_name = form_data.first_name
    db_item.middle_name = form_data.middle_name
    db_item.last_name = form_data.last_name
    db_item.address = form_data.address
    db_item.city = form_data.city
    db_item.state = form_data.state
    db_item.country = form_data.country
    db_item.pin_code = form_data.pin_code
    db_item.contact = form_data.contact
    db_item.email = form_data.email
    db_item.dob = form_data.dob
    db_item.adhar_no = form_data.adhar_no
    db_item.qualification = form_data.qualification
    db_item.designation = form_data.designation
    db_item.date_of_joining = form_data.date_of_joining
    db_item.date_of_leave = form_data.date_of_leave
    db_item.created_at = formatted_datetime
    db_item.updated_at = formatted_datetime
    db_item.created_by = username
    db_item.updated_by = username
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  


def update_staff(db: Session, form_data: ReqUpdateStaffModel, username: str):
    db_item = db.query(Staff).filter(Staff.id == form_data.id).first()
    if db_item:
        db_item.first_name = form_data.first_name
        db_item.middle_name = form_data.middle_name
        db_item.last_name = form_data.last_name
        db_item.address = form_data.address
        db_item.city = form_data.city
        db_item.state = form_data.state
        db_item.country = form_data.country
        db_item.pin_code = form_data.pin_code
        db_item.contact = form_data.contact
        db_item.email = form_data.email
        db_item.dob = form_data.dob
        db_item.adhar_no = form_data.adhar_no
        db_item.qualification = form_data.qualification
        db_item.designation = form_data.designation
        db_item.date_of_joining = form_data.date_of_joining
        db_item.date_of_leave = form_data.date_of_leave
        db_item.updated_at = formatted_datetime
        db_item.updated_by = username
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def delete_staff(db: Session, id: int):
    db_item = db.query(Staff).filter(Staff.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    else:
        return None
