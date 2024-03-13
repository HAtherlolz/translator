import os
import shutil

from pathlib import Path
from typing import NoReturn
from fastapi import UploadFile

from config.conf import settings


async def save_the_file(file: UploadFile) -> str:
    upload_path = Path(settings.UPLOAD_DIRECTORY) / file.filename
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file.filename


async def delete_file(file_name: str) -> NoReturn:
    path = f"{settings.UPLOAD_DIRECTORY}/{file_name}"

    if os.path.exists(path):
        os.remove(path)
        print("File deleted successfully")
    else:
        print("File not found")
