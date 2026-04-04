from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.doctor import Doctor

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ GET ALL (optional filter)
@router.get("/")
def get_doctors(
    specialization: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Doctor)

    if specialization:
        query = query.filter(
            Doctor.specialization.ilike(f"%{specialization}%")
        )

    return query.all()


# ✅ SEARCH BY NAME
@router.get("/search/by-name")
def get_doctor_by_name(name: str, db: Session = Depends(get_db)):
    doctors = db.query(Doctor).filter(
        Doctor.name.ilike(f"%{name}%")
    ).all()

    return doctors


# ✅ SEARCH BY LOCATION
@router.get("/search/by-location")
def get_doctor_by_location(location: str, db: Session = Depends(get_db)):
    doctors = db.query(Doctor).filter(
        Doctor.location.ilike(f"%{location}%")
    ).all()

    return doctors


# ✅ GET BY ID (KEEP LAST)
@router.get("/{doctor_id}")
def get_doctor_by_id(doctor_id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


# ✅ CREATE DOCTOR
@router.post("/create")
def create_doctor(
    name: str,
    specialization: str,
    experience: int,
    rating: float,
    consultation_fee: int,
    location: str,
    db: Session = Depends(get_db)
):
    doctor = Doctor(
        name=name,
        specialization=specialization,
        experience=experience,
        rating=rating,
        consultation_fee=consultation_fee,
        location=location
    )

    db.add(doctor)
    db.commit()
    db.refresh(doctor)

    return {
        "message": "Doctor created successfully",
        "doctor": doctor
    }