from sqlalchemy import Column, ForeignKey, Integer, String
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))


class ResItems(BaseModel):
    id: int
    title: str
    description: str