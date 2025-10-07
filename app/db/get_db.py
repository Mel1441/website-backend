from sqlalchemy.orm import Session
from app.database import SessionLocal

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()