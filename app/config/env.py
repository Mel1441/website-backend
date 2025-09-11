import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from project root
env_file = ".env.prod" if os.getenv("ENV") == "prod" else ".env.dev"
load_dotenv(dotenv_path=env_file)

class Settings:
    ENV: str = os.getenv("ENV", "dev")
    DEBUG: bool = ENV == "dev"

    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "insecure-dev-key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # CORS
    ALLOWED_ORIGINS: list[str] = os.getenv("ALLOWED_ORIGINS", "").split(",")

  
    DATABASE_URL = os.getenv("DATABASE_URL_INTERNAL" if ENV == "prod" else "DATABASE_URL_EXTERNAL")

        # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG" if DEBUG else "INFO")

settings = Settings()
