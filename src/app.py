from fastapi import FastAPI
from src.config import get_settings
from fastapi.middleware.cors import CORSMiddleware
from src.routers import (
    sentiment,
    emotion,
    cover_description
)

SETTINGS = get_settings()
app = FastAPI(title=SETTINGS.api_name, version=SETTINGS.revision)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(sentiment.router)
app.include_router(emotion.router)
app.include_router(cover_description.router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)