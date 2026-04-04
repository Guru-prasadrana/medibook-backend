# 🏥 Medibook Backend

A FastAPI-based backend for managing doctor appointments, AI analysis, slots, and authentication.

---

## 🚀 Features

- 🔐 Authentication (Login/Register)
- 👨‍⚕️ Doctor Management
- 📅 Appointment Booking
- ⏰ Slot Management
- 🤖 AI Analysis (Symptom-based)
- 📊 Database Integration

---

## 🛠️ Tech Stack

- FastAPI
- Python
- SQLAlchemy
- SQLite / PostgreSQL
- Pydantic

---

## 📂 Project Structure


app/
├── api/
│ ├── auth.py
│ ├── doctor.py
│ ├── appointment.py
│ ├── slot.py
│ ├── ai.py
├── db/
│ ├── base.py
│ ├── session.py
├── models/
├── schemas/
├── services/


---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/medibook-backend.git
cd medibook-backend
pip install -r requirements.txt
▶️ Run Server
uvicorn main:app --reload
🌐 API Docs

After running:

Swagger UI → http://127.0.0.1:8000/docs
ReDoc → http://127.0.0.1:8000/redoc
📌 Future Improvements
Payment Integration
Notification System
AI Chatbot Enhancement
👨‍💻 Author

Guruprasad


---

## 💡 Pro Tip
After adding README:
- Your GitHub repo will look **professional**
- Useful for interviews 🔥
- Helps others understand your project quickly

---

If you want, I can also:
✅ Make a **professional GitHub profile README**  
✅ Add **badges (build, version, etc.)**  
✅ Create **API documentation page UI**

Just tell me 👍
