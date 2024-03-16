from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.database import Base

class Test(Base):
    __tablename__ = "tests"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class ReqTestModel(BaseModel):
    name: str


class ResTestModel(BaseModel):
    id: int
    name: str
