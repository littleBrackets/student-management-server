from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

current_datetime = datetime.now()

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    password = Column(String)
    created_at = Column(Date, default=current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(Date, default=current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    status = Column(String, default="PENDING")