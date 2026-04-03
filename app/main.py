from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api import ai
from app.api import doctor
from app.api import slot
from app.api import appointment


# 👉 IMPORT ROUTER
from app.api import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

# 👉 INCLUDE ROUTER
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])
app.include_router(doctor.router, prefix="/doctors", tags=["Doctors"])
app.include_router(slot.router, prefix="/slots", tags=["Slots"])
app.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}