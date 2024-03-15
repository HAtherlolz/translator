from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from config.databases import init_db, ping_db
from config.conf import settings
from app.api.router import router
from app.api.ws.ws_router import ws_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = await init_db()
    await ping_db(client)
    print("Starting up")
    yield
    print("Shutting down")


app = FastAPI(
    openapi_url="/api/v1/",
    docs_url="/api/v1/docs/",
    redoc_url="/api/v1/redoc/",
    title="Vacancies parsers",
    description="Backend for vacancies parsers",
    version="0.1",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(ws_router)
