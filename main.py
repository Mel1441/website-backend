from fastapi import FastAPI
from config.cors import add_cors
from routes import include_all_routes



app = FastAPI(title="Modular Backend")

@app.get("/ping")
def ping():
    return {"message": "Direct ping works!"}

add_cors(app)

include_all_routes(app)