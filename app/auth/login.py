from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import bcrypt, jwt, datetime

router = APIRouter()
#from dotenv import load_dotenv
#load_dotenv()
#SECRET = os.getenv("JWT_SECRET")

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(req: LoginRequest):
    # Dummy user for demo
    user_db = {"melissa_kid": bcrypt.hashpw(b"secure123", bcrypt.gensalt())}

    if req.username not in user_db:
        raise HTTPException(status_code=401, detail="Invalid username")

    if not bcrypt.checkpw(req.password.encode(), user_db[req.username]):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = jwt.encode({
        "sub": req.username,
        "role": "child",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, SECRET, algorithm="HS256")

    with open("logs/login_audit.log", "a") as log:
        log.write(f"[{datetime.datetime.now()}] LOGIN: {req.username}\n")

    return {"status": "success", "token": token, "role": "child"}