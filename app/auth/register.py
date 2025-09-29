from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

auth_router = APIRouter()

class RegisterPayload(BaseModel):
    email: str
    password: str
    role: str
    school_id: str | None = None
    curriculum_tag: str | None = None

@auth_router.post("/auth/register")
def register_user(payload: RegisterPayload):
    # 1. Check if user already exists
    # 2. Hash password securely
    # 3. Store user in DB with role, school_id, curriculum_tag
    # 4. Return success or error
    return {"message": "User registered successfully"}