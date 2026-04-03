from sqlalchemy import Column, Integer, String
from app.db.base import Base

class SymptomLog(Base):
    __tablename__ = "symptom_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    symptoms_text = Column(String)
    predicted_specialization = Column(String)