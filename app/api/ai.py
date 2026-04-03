from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.ai_service import analyze_symptoms
from app.models.symptom_log import SymptomLog
from app.models.doctor import Doctor

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/analyze")
def analyze(symptoms: str, user_id: int, db: Session = Depends(get_db)):

    # 🔥 Step 1: AI analyze
    result = analyze_symptoms(symptoms)

    specialization = result["specialty"]

    # 🔥 Step 2: Save log
    log = SymptomLog(
        user_id=user_id,
        symptoms_text=symptoms,
        predicted_specialization=specialization
    )
    db.add(log)
    db.commit()

    # 🔥 Step 3: Fetch doctors from DB
    doctors = db.query(Doctor).filter(
        Doctor.specialization.ilike(f"%{specialization}%")
    ).all()

    # 🔥 Step 4: Format doctor response
    doctor_list = [
        {
            "id": d.id,
            "name": d.name,
            "specialization": d.specialization,
            "experience": d.experience,
            "rating": d.rating,
            "fee": d.consultation_fee
        }
        for d in doctors
    ]

    # 🔥 FINAL RESPONSE
    return {
        "specialization": specialization,
        "confidence": result["confidence"],
        "matched_keywords": result["matched_keywords"],
        "doctors": doctor_list,   # ✅ THIS IS YOUR MAIN FEATURE
        "user_id": user_id,
        "message": "This is not a medical diagnosis. Please consult a doctor."
    }