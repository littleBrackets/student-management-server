from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.database import Base

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class ReqSubjectModel(BaseModel):
    name: str


class ResSubjectModel(BaseModel):
    id: int
    name: str
