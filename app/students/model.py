from sqlalchemy import Column, Integer, String, Date, DateTime
from pydantic import BaseModel
from app.database import Base
from datetime import datetime, date

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    pin_code = Column(Integer)
    contact = Column(Integer)
    email = Column(String)
    dob = Column(Date)
    adhar_no = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    created_by = Column(String)
    updated_by = Column(String)


class ReqStudentModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    address: str
    city: str
    state: str
    country: str
    pin_code: int
    contact: int
    email: str
    dob: date
    adhar_no: int


class ResStudentModel(BaseModel):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    address: str
    city: str
    state: str
    country: str
    pin_code: int
    contact: int
    email: str
    dob: date
    adhar_no: int
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str


class ReqUpdateStudentModel(BaseModel):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    address: str
    city: str
    state: str
    country: str
    pin_code: int
    contact: int
    email: str
    dob: date
    adhar_no: int
