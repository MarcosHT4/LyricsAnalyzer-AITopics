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
from src.db import SongAnalysisProfile
from src.db import get_session
from src.schemas.execution import Execution

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
def analyze_emotion(song:SongInput = Body(...), song_division = Depends(get_song_division_service), song_emotion = Depends(get_song_emotion_analysis_service),  db_session = Depends(get_session)) -> SongAnalysisOutput:
    start = time.time()
    song_structure_output = song_division.divide_song_into_sections(song.lyrics)
    song_emotions_output = song_emotion.predict(song_structure_output)
    execution = Execution(time_in_seconds=time.time() - start, models_used=[SETTINGS.models_names[1]], lyrics_char_length=len(song.lyrics), version_number=SETTINGS.revision)
    output = SongAnalysisOutput(name=song.name, artist=song.artist, analysis=song_emotions_output, execution=execution)
    profile = SongAnalysisProfile(song_title=song.name, artist_name=song.artist, emotion=song_emotions_output.dict())
    db_session.add(profile)
    db_session.commit()
    db_session.refresh(profile)
    return output