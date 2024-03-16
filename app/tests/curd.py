from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from .model import Test, ReqTestModel, ResTestModel


def get_test_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Test).offset(skip).limit(limit).all()


def get_test_by_id(db: Session, id: int):
    return db.query(Test).filter(Test.id == id).first()


def create_test(db: Session,  form_data: ReqTestModel):
    db_item = Test(name=form_data.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  


def update_test(db: Session, form_data: ResTestModel):
    db_item = db.query(Test).filter(Test.id == form_data.id).first()
    if db_item:
        db_item.name = form_data.name
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


def delete_test(db: Session, id: int):
    db_item = db.query(Test).filter(Test.id == id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    else:
        return None
