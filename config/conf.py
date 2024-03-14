import os

from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()


class Settings(BaseConfig):
    UPLOAD_DIRECTORY = "app/files"

    OPENAI_TOKEN: str = os.getenv("OPENAI_TOKEN")
    OPENAI_VERSION: str = os.getenv("OPENAI_VERSION")
    ASSEMBLYAI_TOKEN: str = os.getenv("ASSEMBLYAI_TOKEN")

    # DATABASE creds
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_CLUSTER: str = os.getenv("DB_CLUSTER")

    # Allowed hosts
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8000",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8080",
    ]


settings = Settings()
