from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.services.otp_service import generate_otp
from app.services.sms_service import send_sms
router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/send-otp")
def send_otp(phone: str, db: Session = Depends(get_db)):
    otp = generate_otp()

    user = db.query(User).filter(User.phone == phone).first()

    if not user:
        user = User(phone=phone, otp=otp)
        db.add(user)
    else:
        user.otp = otp

    db.commit()

    # ✅ SAFE CALL
    try:
        send_sms(phone, otp)
    except Exception as e:
        print("Twilio Error:", e)

    return {
        "message": "OTP sent successfully",
        "otp": otp   # keep for testing
    }

# 🔹 VERIFY OTP (ADD HERE 👇)
@router.post("/verify-otp")
def verify_otp(phone: str, otp: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()

    if not user or user.otp != otp:
        return {"error": "Invalid OTP"}

    return {
        "message": "Login successful",
        "user_id": user.id
    }