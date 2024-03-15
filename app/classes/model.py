from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.database import Base
from datetime import datetime, date

current_datetime = datetime.now()

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class ReqClassModel(BaseModel):
    name: str


class ResClassModel(BaseModel):
    id: int
    name: str
