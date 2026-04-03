from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.appointment import Appointment
from app.models.slot import Slot

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def book_appointment(user_id: int, doctor_id: int, slot_id: int, db: Session = Depends(get_db)):
    
    # 🔥 STEP 1: check slot exists
    slot = db.query(Slot).filter(Slot.id == slot_id).first()

    if not slot:
        return {"error": "Slot not found"}

    # 🔥 STEP 2: prevent double booking
    if slot.is_booked:
        return {"error": "Slot already booked"}

    # 🔥 STEP 3: mark slot as booked
    slot.is_booked = True

    # 🔥 STEP 4: create appointment
    appointment = Appointment(
        user_id=user_id,
        doctor_id=doctor_id,
        slot_id=slot_id
    )

    db.add(appointment)
    db.commit()

    return {
        "message": "Appointment booked successfully",
        "appointment_id": appointment.id
    }