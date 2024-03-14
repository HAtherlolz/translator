from uuid import UUID, uuid4
from pydantic import Field
from typing import Optional, List

from beanie import Document, Indexed


class User(Document):
    name: str
    second_name: Optional[str]
    uuid: UUID = Field(default_factory=uuid4)


class Room(Document):
    room_uuid: UUID = Field(default_factory=uuid4)
    users: List[User]

