from sqlalchemy import Column, Integer, String, Date, DateTime
from pydantic import BaseModel
from app.database import Base
from datetime import datetime, date

class Staff(Base):
    __tablename__ = "staffs"
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
    qualification = Column(String)
    designation = Column(String)
    date_of_joining = Column(Date)
    date_of_leave = Column(Date)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    created_by = Column(String)
    updated_by = Column(String)


class ReqStaffModel(BaseModel):
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
    qualification: str
    designation: str
    date_of_joining: date
    date_of_leave: date



class ResStaffModel(BaseModel):
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
    qualification: str
    designation: str
    date_of_joining: date
    date_of_leave: date
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str


class ReqUpdateStaffModel(BaseModel):
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
    qualification: str
    designation: str
    date_of_joining: date
    date_of_leave: date
