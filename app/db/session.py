# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://postgres:12345@localhost:5432/medibook"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load .env for local
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"} if "render.com" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(bind=engine)