from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.doctor import Doctor

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_doctors(specialization: str, db: Session = Depends(get_db)):
    doctors = db.query(Doctor).filter(
        Doctor.specialization.ilike(f"%{specialization}%")
    ).all()

    return doctors

@router.post("/create")
def create_doctor(
    name: str,
    specialization: str,
    experience: int,
    rating: float,
    consultation_fee: int,
    db: Session = Depends(get_db)
):
    doctor = Doctor(
        name=name,
        specialization=specialization,
        experience=experience,
        rating=rating,
        consultation_fee=consultation_fee
    )

    db.add(doctor)
    db.commit()

    return {"message": "Doctor created"}