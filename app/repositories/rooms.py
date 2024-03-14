import uuid

from typing import Optional

from fastapi import HTTPException

from app.schemas.models import User, Room
from app.schemas.rooms import UserCreate, UserSchema, RoomSchema


async def save_user(user: UserSchema) -> User:
    print("===== user.uuid =========", type(user.uuid))
    user = User(name=user.name, second_name=user.second_name, uuid=user.uuid)
    return await user.insert()


async def get_user(uuid: str) -> User:
    user = await User.find_one(User.uuid == uuid)
    return user


async def save_room(user_uuid: str) -> Room:
    user = await get_user(user_uuid)

    print(user)
    room = Room(users=[user], room_uuid=str(uuid.uuid4()), creator=user)
    room = await room.insert()
    return room


async def get_room(room_uuid: str) -> Optional[Room]:
    room = await Room.find_one(Room.room_uuid == room_uuid)
    if not room:
        raise HTTPException(status_code=400, detail="Room with this uuid does not exist")

    return room


# async def add_user_to_room()