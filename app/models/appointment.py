from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.base import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    slot_id = Column(Integer, ForeignKey("slots.id"))
    status = Column(String, default="booked")