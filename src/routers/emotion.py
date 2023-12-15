from fastapi import (
    APIRouter,
    Depends,
    Body
)
import time
from functools import cache
from src.config import get_settings
from src.schemas.song_input import SongInput
from src.services.song_division_service import SongDivisionService
from src.services.song_emotion_analysis_service import SongEmotionAnalysisService
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.song_analysis_output import SongAnalysisOutput

router = APIRouter()
SETTINGS  = get_settings()
song_division_service = SongDivisionService()
song_emotion_analysis_service = SongEmotionAnalysisService()

@cache
def get_song_division_service():
    return song_division_service

@cache
def get_song_emotion_analysis_service():
    return song_emotion_analysis_service

@router.post("/emotion")
def analyze_emotion(song:SongInput = Body(...), song_division = Depends(get_song_division_service), song_emotion = Depends(get_song_emotion_analysis_service)) -> SongAnalysisOutput:
    start = time.time()
    song_structure_output = song_division.divide_song_into_sections(song.lyrics)
    song_emotions_output = song_emotion.predict(song_structure_output)
    output = SongAnalysisOutput(name=song.name, artist=song.artist, analysis=song_emotions_output)
    return output