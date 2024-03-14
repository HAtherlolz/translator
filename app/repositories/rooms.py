from app.schemas.models import User, Room
from app.schemas.rooms import UserCreate, UserSchema, RoomSchema


async def save_room(user: UserSchema) -> Room:
    user = User(name=user.name, second_name=user.second_name)

    saved_user = await user.insert()

    room = Room(users=[saved_user])
    room = await room.insert()
    return room
