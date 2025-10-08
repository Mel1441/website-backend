from fastapi.middleware.cors import CORSMiddleware

def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:1000", "https://mmason.tech", "https://api.mmason.tech"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )