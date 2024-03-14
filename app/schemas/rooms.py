from datetime import datetime

from uuid import UUID

from typing import Optional, List
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    second_name: Optional[str]


class UserSchema(UserCreate):
    uuid: str
    date_created: datetime = datetime.now()


class RoomSchema(BaseModel):
    room_uuid: str
    users: List[UserSchema]
    creator: UserSchema
    date_created: datetime = datetime.now()

