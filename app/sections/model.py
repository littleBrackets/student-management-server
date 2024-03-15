from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.database import Base

class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class ReqSectionModel(BaseModel):
    name: str


class ResSectionModel(BaseModel):
    id: int
    name: str
