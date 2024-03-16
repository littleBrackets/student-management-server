from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from app.database import Base
from datetime import datetime

class Institute(Base):
    __tablename__ = "institutes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    pin_code = Column(Integer)
    contact = Column(Integer)
    email = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    created_by = Column(String)
    updated_by = Column(String)


class ReqInstituteModel(BaseModel):
    name: str
    address: str
    city: str
    state: str
    country: str
    pin_code: int
    contact: int
    email: str


class ResInstituteModel(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    country: str
    pin_code: int
    contact: int
    email: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str


class ReqUpdateInstituteModel(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    country: str
    pin_code: int
    contact: int
    email: str