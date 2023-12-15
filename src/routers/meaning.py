from fastapi import (
    APIRouter,
    Depends,
    Body
)
import time
from functools import cache
from src.config import get_settings
from src.schemas.song_input import SongInput
from src.schemas.song_meaning_output import SongMeaningOutput
from src.services.song_division_service import SongDivisionService
from src.services.song_meaning_analysis_service import SongMeaningAnalysisService
from src.schemas.song_analysis_output import SongAnalysisOutput

router = APIRouter()
SETTINGS = get_settings()
song_division_service = SongDivisionService()
song_meaning_analysis_service = SongMeaningAnalysisService()


@cache
def get_song_division_service():
    return song_division_service

@cache
def get_song_meaning_analysis_service():
    return song_meaning_analysis_service

@router.post("/meaning")
def analyze_song_meaning(song:SongInput = Body(...), song_division = Depends(get_song_division_service), song_meaning_analysis = Depends(get_song_meaning_analysis_service)) -> SongAnalysisOutput:
    start = time.time()
    song_structure_output = song_division.divide_song_into_sections(song.lyrics)
    meaning_output = song_meaning_analysis.predict(song_structure_output)
    output = SongAnalysisOutput(name=song.name, artist=song.artist, meaning=meaning_output)
    return output
