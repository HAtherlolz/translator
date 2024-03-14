from fastapi import APIRouter

from app.schemas.models import Room, User
from app.schemas.rooms import UserSchema, UserCreate
from app.services.rooms import room_creation, user_creation

api_rooms = APIRouter()


@api_rooms.post("/room/user/", response_model=User, status_code=200)
async def create_user(
        user: UserCreate
):
    return await user_creation(user)


@api_rooms.post("/room/", response_model=Room, status_code=200)
async def create_room(
        user_uuid: str
):
    return await room_creation(user_uuid)
