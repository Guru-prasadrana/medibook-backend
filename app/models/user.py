# models/user.py

from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True, index=True)
    name = Column(String, nullable=True)

    otp = Column(String, nullable=True)