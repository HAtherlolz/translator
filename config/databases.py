from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .conf import settings
from app.schemas.models import User, Room


db_url = f"mongodb+srv://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_CLUSTER}/?retryWrites=true&w=majority"


async def init_db() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(db_url)
    await init_beanie(database=client.db_name, document_models=[User, Room])
    return client


async def ping_db(client):
    """ Check db connection """
    try:
        client.admin.command('ping')
        print("Connected to database")
    except Exception as e:
        print("DB wasn't connected: ", e)
