from pydantic import BaseModel


class ResponseTranslate(BaseModel):
    language: str
    text: str
