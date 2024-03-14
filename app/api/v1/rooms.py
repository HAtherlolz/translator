from fastapi import APIRouter

from app.schemas.models import Room
from app.schemas.rooms import RoomSchema, UserCreate
from app.services.rooms import room_creation

api_rooms = APIRouter()


@api_rooms.post("/room/", response_model=Room, status_code=200)
async def create_room(
        user: UserCreate
):
    return await room_creation(user)
