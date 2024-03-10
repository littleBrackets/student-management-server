from sqlalchemy import Column, String, Date
from pydantic import BaseModel
from app.database import Base
from datetime import datetime, date

current_datetime = datetime.now()

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True)
    password = Column(String)
    created_at = Column(Date, default=current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(Date, default=current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    status = Column(String, default="PENDING")


class ReqUserSignupModel(BaseModel):
    username: str
    password: str


class ReqUserLoginModel(BaseModel):
    username: str
    password: str


class ResUserModel(BaseModel):
    username: str
    created_at: date
    updated_at: date
    status: str

