from fastapi import UploadFile

from app.schemas.request import RequestTranslate
from app.schemas.responses import ResponseTranslate
from app.services.files import save_the_file, delete_file
from app.services.chatgpt import translate as tr
from app.services.asseblyai import get_text_from_audio


async def translate_from_file(audio: UploadFile, lang_from: str, lang_to: str) -> ResponseTranslate:
    saved_file = await save_the_file(audio)
    data = await get_text_from_audio(saved_file, lang_from)
    text = await tr(data, lang_to)
    await delete_file(saved_file)
    return ResponseTranslate(language=lang_to, text=text)


async def translate_from_text(body: RequestTranslate) -> ResponseTranslate:
    text = await tr(body.text, body.language_to)
    return ResponseTranslate(language=body.language_to, text=text)







