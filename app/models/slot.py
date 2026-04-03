from sqlalchemy import Column, Integer, ForeignKey, Date, Time, Boolean
from app.db.base import Base

class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    date = Column(Date)
    time = Column(Time)
    is_booked = Column(Boolean, default=False)