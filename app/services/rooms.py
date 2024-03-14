import uuid

from app.schemas.models import Room
from app.schemas.rooms import UserCreate, UserSchema, RoomSchema
from app.repositories.rooms import save_room


async def room_creation(user: UserCreate) -> Room:
    user = UserSchema(name=user.name, second_name=user.second_name, uuid=uuid.uuid4())
    return await save_room(user)
