from fastapi import (
    APIRouter,
    Depends,
    Body
)
import time
import httpx
from functools import cache
from src.config import get_settings
from src.services.song_division_service import SongDivisionService
from src.services.song_emotion_analysis_service import SongEmotionAnalysisService
from src.services.genius_scrapping_service import GeniusScrappingService
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.song_analysis_output import SongAnalysisOutput
from src.db import SongAnalysisProfile
from src.db import get_session

router = APIRouter()
SETTINGS  = get_settings()
song_division_service = SongDivisionService()
song_emotion_analysis_service = SongEmotionAnalysisService()
genius_scrapping_service = GeniusScrappingService()

def get_http_client():
    return httpx.AsyncClient()

@cache
def get_song_division_service():
    return song_division_service

@cache
def get_song_emotion_analysis_service():
    return song_emotion_analysis_service

@cache
def get_genius_scrapping_service():
    return genius_scrapping_service

@router.post("/emotion_url")
async def analyze_emotion_by_url(song_url:str = Body(..., embed=True), song_division = Depends(get_song_division_service), song_emotion = Depends(get_song_emotion_analysis_service),  genius_scrapping = Depends(get_genius_scrapping_service),client:httpx.AsyncClient = Depends(get_http_client), db_session = Depends(get_session)) -> SongAnalysisOutput:
    start = time.time()
    song = await genius_scrapping.get_song_from_genius(song_url, client)
    song_structure_output = song_division.divide_song_into_sections(song.lyrics)
    song_emotions_output = song_emotion.predict(song_structure_output)
    output = SongAnalysisOutput(name=song.name, artist=song.artist, analysis=song_emotions_output)
    profile = SongAnalysisProfile(song_title=song.name, artist_name=song.artist, emotion=song_emotions_output.dict())
    db_session.add(profile)
    db_session.commit()
    db_session.refresh(profile)
    return output