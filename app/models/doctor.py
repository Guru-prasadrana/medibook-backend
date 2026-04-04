from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    experience = Column(Integer)
    rating = Column(Float)
    consultation_fee = Column(Integer)
    location = Column(String)