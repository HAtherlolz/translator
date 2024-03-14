from fastapi import APIRouter, UploadFile, File, Form

from app.schemas.responses import ResponseTranslate
from app.schemas.request import RequestTranslate
from app.services.audio import translate_from_file, translate_from_text


api_translate = APIRouter()


@api_translate.post("/upload-audio/", response_model=ResponseTranslate, status_code=200)
async def upload_audio(
        language_from: str = Form(...),
        language_to: str = Form(...),
        audio: UploadFile = File(...)
):
    return await translate_from_file(audio, language_from, language_to)


@api_translate.post("/translate/", response_model=ResponseTranslate, status_code=200)
async def translate_txt(
        language_to: str = Form(...),
        text: str = Form(...)
):
    body = RequestTranslate(language_to=language_to, text=text)
    return await translate_from_text(body)
