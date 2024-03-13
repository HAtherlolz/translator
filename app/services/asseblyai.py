import assemblyai as aai
from assemblyai.types import TranscriptionConfig, LanguageCode

from config.conf import settings


async def get_text_from_audio(file_name: str, language_from: str) -> str:
    lg = LanguageCode(language_from)
    conf = TranscriptionConfig(language_code=lg)

    aai.settings.api_key = settings.ASSEMBLYAI_TOKEN

    transcriber = aai.Transcriber(config=conf)
    file_path = f"{settings.UPLOAD_DIRECTORY}/{file_name}"
    transcript = transcriber.transcribe(file_path)

    if transcript.status == aai.TranscriptStatus.error:
        print("Error: ", transcript.error)
    else:
        print(transcript.text)

    return transcript.text
