from fastapi import (
    APIRouter,
    Depends,
    Body,
    File,
    UploadFile
)
import time
from src.config import get_settings
from src.services.profile_generation_service import ProfileGenerationService
from src.services.song_sentiment_analysis_service import SongSentimentAnalysisService
from src.services.song_emotion_analysis_service import SongEmotionAnalysisService
from src.schemas.profile import Profile
from functools import cache
from sqlmodel import Session, select
from src.db import SongAnalysisProfile
from src.db import get_session

router = APIRouter()
SETTINGS = get_settings()

profile_generation_service = ProfileGenerationService()
song_sentiment_analysis_service = SongSentimentAnalysisService()
song_emotion_analysis_service = SongEmotionAnalysisService()

@cache
def get_profile_generation_service():
    return profile_generation_service
@cache
def get_song_sentiment_analysis_service():
    return song_sentiment_analysis_service
@cache
def get_song_emotion_analysis_service():
    return song_emotion_analysis_service

@router.get("/profile")
async def get_profile(profile_generation = Depends(get_profile_generation_service), song_sentiment_analysis = Depends(get_song_sentiment_analysis_service),song_emotion_analysis = Depends(get_song_emotion_analysis_service),db_session = Depends(get_session)) -> Profile:
    song_profiles = profile_generation.generate_profile(db_session, song_sentiment_analysis, song_emotion_analysis)
    return song_profiles
