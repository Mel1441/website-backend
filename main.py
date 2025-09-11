from fastapi import FastAPI
from app.config.cors import add_cors
from routes import include_all_routes
import os
from app.config.env import settings

if settings.DEBUG:
    print("Running in development mode")

app = FastAPI(debug=settings.DEBUG)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"



app = FastAPI(title="Modular Backend")

@app.get("/ping")
def ping():
    return {"message": "Direct ping works!"}

add_cors(app)

include_all_routes(app)