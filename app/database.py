from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

env_file = ".env.development" if os.getenv("ENV") == "development" else ".env.production"
load_dotenv(dotenv_path=env_file)

DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()