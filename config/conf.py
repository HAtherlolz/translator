import os

from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()


class Settings(BaseConfig):
    UPLOAD_DIRECTORY = "app/files"

    OPENAI_TOKEN: str = os.getenv("OPENAI_TOKEN")
    OPENAI_VERSION: str = os.getenv("OPENAI_VERSION")
    ASSEMBLYAI_TOKEN: str = os.getenv("ASSEMBLYAI_TOKEN")

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
