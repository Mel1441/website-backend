from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config.cors import add_cors
from routes import include_all_routes
import os
from app.config.env import settings
from app.routes.auth import router as auth_router


if settings.DEBUG:
    print("Running in development mode")

app = FastAPI(debug=settings.DEBUG)

app.mount("/", StaticFiles(directory="fe/dist", html=True), name="static")


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"



#app = FastAPI(title="Modular Backend")

@app.get("/ping")
def ping():
    return {"message": "Direct ping works!"}

# app/main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class VisitPayload(BaseModel):
    page: str
    timestamp: str

@app.post("/track-visit")
async def track_visit(payload: VisitPayload, request: Request):
    ip = request.client.host
    print(f"🔍 Visit tracked: {payload.page} at {payload.timestamp} from {ip}")

    # ✅ Log to file
    with open("visit_log.txt", "a") as f:
        f.write(f"{payload.page},{payload.timestamp},{ip}\n")

    return {"status": "ok"}

add_cors(app)

include_all_routes(app)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
