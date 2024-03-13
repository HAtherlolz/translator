from fastapi import UploadFile

from app.schemas.responses import ResponseTranslate
from app.services.files import save_the_file, delete_file
from app.services.chatgpt import translate as tr
from app.services.asseblyai import get_text_from_audio


async def translate_from_file(audio: UploadFile, lang_from: str, lang_to: str) -> ResponseTranslate:
    saved_file = await save_the_file(audio)
    data = await get_text_from_audio(saved_file, lang_from)
    await delete_file(saved_file)
    text = await tr(data, lang_to)
    return ResponseTranslate(language=lang_to, text=text)


async def translate_from_text(lang_to: str, text: str) -> ResponseTranslate:
    text = await tr(text, lang_to)
    return ResponseTranslate(language=lang_to, text=text)







