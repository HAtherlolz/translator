import os

from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()


class Settings(BaseConfig):
    UPLOAD_DIRECTORY = "app/files"

    OPENAI_TOKEN: str = os.getenv("OPENAI_TOKEN")
    ASSEMBLYAI_TOKEN: str = os.getenv("ASSEMBLYAI_TOKEN")


settings = Settings()
