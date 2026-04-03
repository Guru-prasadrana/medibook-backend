from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ ADD THIS

from app.db.base import Base
from app.db.session import engine
from app.api import ai, doctor, slot, appointment, auth

app = FastAPI()

# ✅ ADD CORS HERE (VERY IMPORTANT POSITION)
origins = [
    "http://localhost:3000",  # frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # ❗ NOT "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])
app.include_router(doctor.router, prefix="/doctors", tags=["Doctors"])
app.include_router(slot.router, prefix="/slots", tags=["Slots"])
app.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}