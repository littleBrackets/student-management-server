from sqlalchemy import Column, ForeignKey, Integer, String, Date
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, date

current_datetime = datetime.now()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(Date, default=current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(Date, default=current_datetime.strftime("%Y-%m-%d %H:%M:%S"))


class ReqItemModel(BaseModel):
    id: int
    title: str
    description: str


class ResItemModel(BaseModel):
    id: int
    title: str
    description: str
    created_at: date
    updated_at: date
