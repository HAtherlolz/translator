from datetime import datetime

from uuid import UUID, uuid4
from pydantic import Field
from typing import Optional, List

from beanie import Document, Indexed


class User(Document):
    name: str
    second_name: Optional[str]
    uuid: Indexed(str, unique=True)
    date_created: datetime = datetime.now()


class Room(Document):
    room_uuid: Indexed(str, unique=True)
    users: List[User]
    creator: User
    date_created: datetime = datetime.now()


