from sqlalchemy.orm import declarative_base

Base = declarative_base()

# 🔥 ADD THIS (VERY IMPORTANT)
from app.models.user import User
from app.models.doctor import Doctor
from app.models.slot import Slot
from app.models.appointment import Appointment
from app.models.symptom_log import SymptomLog