from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.slot import Slot

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{doctor_id}")
def get_slots(doctor_id: int, db: Session = Depends(get_db)):
    slots = db.query(Slot).filter(
        Slot.doctor_id == doctor_id
    ).all()

    return slots

@router.post("/create")
def create_slot(
    doctor_id: int,
    date: str,
    time: str,
    db: Session = Depends(get_db)
):
    slot = Slot(
        doctor_id=doctor_id,
        date=date,
        time=time,
        is_booked=False
    )

    db.add(slot)
    db.commit()

    return {"message": "Slot created"}