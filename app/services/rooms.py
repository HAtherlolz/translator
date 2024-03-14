import uuid

from app.schemas.models import Room, User
from app.schemas.rooms import UserCreate, UserSchema, RoomSchema
from app.repositories.rooms import save_room, save_user


async def user_creation(user: UserCreate) -> User:
    user = UserSchema(name=user.name, second_name=user.second_name, uuid=str(uuid.uuid4()))
    return await save_user(user)


async def room_creation(user_uuid: str) -> Room:
    return await save_room(user_uuid)
