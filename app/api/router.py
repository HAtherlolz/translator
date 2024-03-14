from fastapi import APIRouter

from app.api.v1.audio_file import api_translate
from app.api.v1.rooms import api_rooms


router = APIRouter()

router.include_router(api_rooms, prefix="/api/v1", tags=["rooms"])
router.include_router(api_translate, prefix="/api/v1", tags=["audio"])
