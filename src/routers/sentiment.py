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
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.song_input import SongInput
from src.schemas.song_analysis_output import SongAnalysisOutput
from src.db import SongAnalysisProfile
from src.db import get_session


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
def analyze_sentiment(song:SongInput = Body(...), song_division = Depends(get_song_division_service), song_sentiment_analysis = Depends(get_song_sentiment_analysis_service),  db_session = Depends(get_session)) -> SongAnalysisOutput:
    start = time.time()
    song_structure_output = song_division.divide_song_into_sections(song.lyrics)
    sentiment_output = song_sentiment_analysis.predict(song_structure_output)
    output = SongAnalysisOutput(name=song.name, artist=song.artist, analysis=sentiment_output)
    profile = SongAnalysisProfile(song_title=song.name, artist_name=song.artist, sentiment=sentiment_output.dict())
    db_session.add(profile)
    db_session.commit()
    db_session.refresh(profile)
    return output
