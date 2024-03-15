from fastapi import APIRouter

from app.api.ws.rooms import ws_router as wsr


ws_router = APIRouter(prefix="/api", tags=["ws"])

ws_router.include_router(wsr)
