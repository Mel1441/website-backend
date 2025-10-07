from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

env_file = ".env.development" if os.getenv("ENV") == "development" else ".env.production"
load_dotenv(dotenv_path=env_file)
print(env_file)
def get_engine():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL not set")
    return create_engine(db_url, echo=True, future=True)

#DB_URL = os.getenv("DATABASE_URL")
#print(DB_URL)
#engine = create_engine(DB_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=get_engine(), autocommit=False, autoflush=False)

Base = declarative_base()