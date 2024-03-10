from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    disabled = Column(Boolean, default=False)