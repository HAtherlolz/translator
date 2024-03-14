from pydantic import BaseModel


class RequestTranslate(BaseModel):
    language_to: str
    text: str
