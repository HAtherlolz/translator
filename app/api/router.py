from fastapi import APIRouter

from app.api.v1.audio_file import api_translate


router = APIRouter()

router.include_router(api_translate, prefix="/api/v1", tags=["audio"])
