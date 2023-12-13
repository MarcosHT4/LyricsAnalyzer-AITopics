from fastapi import (
    APIRouter,
    Depends,
    Body
)
import time
import httpx
from functools import cache
from src.config import get_settings
from src.schemas.song_input import SongInput
from src.schemas.song_meaning_output import SongMeaningOutput
from src.services.genius_scrapping_service import GeniusScrappingService
from src.services.song_division_service import SongDivisionService
from src.services.song_meaning_analysis_service import SongMeaningAnalysisService

router = APIRouter()
SETTINGS = get_settings()
song_division_service = SongDivisionService()
song_meaning_analysis_service = SongMeaningAnalysisService()
genius_scrapping_service = GeniusScrappingService()

def get_http_client():
    return httpx.AsyncClient()

@cache
def get_song_division_service():
    return song_division_service

@cache
def get_song_meaning_analysis_service():
    return song_meaning_analysis_service

@cache
def get_genius_scrapping_service():
    return genius_scrapping_service

@router.post("/meaning_url")
async def analyze_song_meaning_by_url(song_url:str = Body(...), song_division = Depends(get_song_division_service), song_meaning_analysis = Depends(get_song_meaning_analysis_service), genius_scrapping = Depends(get_genius_scrapping_service), client:httpx.AsyncClient = Depends(get_http_client)) -> SongMeaningOutput:
    start = time.time()
    song = await genius_scrapping.get_song_from_genius(song_url, client)
    song_structure_output = song_division.divide_song_into_sections(song.lyrics)
    output = song_meaning_analysis.predict(song_structure_output)
    return output