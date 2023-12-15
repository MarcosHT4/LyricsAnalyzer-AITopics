from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config import get_settings
from fastapi.middleware.cors import CORSMiddleware
from src.routers import (
    status,
    sentiment,
    emotion,
    cover_description,
    sentiment_url,
    emotion_url,
    meaning,
    meaning_url,
    analysis,
    analysis_url,
    profile_generation
)

from src.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    create_db_and_tables()
    yield

SETTINGS = get_settings()
app = FastAPI(title=SETTINGS.api_name, version=SETTINGS.revision, lifespan=lifespan)


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(status.router)
app.include_router(sentiment.router)
app.include_router(emotion.router)
app.include_router(meaning.router)
app.include_router(cover_description.router)
app.include_router(sentiment_url.router)
app.include_router(emotion_url.router)
app.include_router(meaning_url.router)
app.include_router(analysis.router)
app.include_router(analysis_url.router)
app.include_router(profile_generation.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)