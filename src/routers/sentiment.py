from fastapi import (
    APIRouter,
    Depends,
    Body
)
import time
from functools import cache
from src.config import get_settings
from src.services.song_division_service import SongDivisionService
from src.services.song_sentiment_analysis_service import SongSentimentAnalysisService
from src.schemas.song_section_sentiment import SongSectionSentiment
from src.schemas.song_input import SongInput

router = APIRouter()
song_division_service = SongDivisionService()
song_sentiment_analysis_service = SongSentimentAnalysisService()
SETTINGS = get_settings()

@cache
def get_song_division_service():
    return song_division_service
@cache
def get_song_sentiment_analysis_service():
    return song_sentiment_analysis_service

@router.post("/sentiment")
def analyze_sentiment(song:SongInput = Body(...), song_division = Depends(get_song_division_service), song_sentiment_analysis = Depends(get_song_sentiment_analysis_service)) -> SongSectionSentiment:
    start = time.time()
    song_structure_output = song_division.divide_song_into_sections(song.lyrics)
    output = song_sentiment_analysis.predict(song_structure_output)
    return output
