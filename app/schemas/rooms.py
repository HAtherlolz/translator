from uuid import UUID

from typing import Optional, List
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    second_name: Optional[str]


class UserSchema(UserCreate):
    uuid: Optional[UUID]


class RoomSchema(BaseModel):
    room_uuid: Optional[UUID]
    users: List[UserSchema]

