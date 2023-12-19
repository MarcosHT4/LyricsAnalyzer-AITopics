from fastapi import (
    APIRouter,
    Depends,
    Body,
    File,
    UploadFile
)
import time
from sqlmodel import Session, select
from functools import cache
from src.config import get_settings
from src.schemas.song_input import SongInput
from src.schemas.song_meaning_output import SongMeaningOutput
from src.schemas.song_full_analysis_output import SongFullAnalysisOutput
from src.db import SongAnalysisProfile
from src.db import get_session
from src.services.song_division_service import SongDivisionService
from src.services.song_sentiment_analysis_service import SongSentimentAnalysisService
from src.services.song_emotion_analysis_service import SongEmotionAnalysisService
from src.services.image_to_base64_service import ImageToBase64Service
from src.services.image_description_service import ImageDescriptionService
from src.services.song_complete_analysis_service import SongCompleteAnalysisService
from sqlmodel import Session, select
from src.db import SongAnalysisProfile
from src.db import get_session
from src.schemas.execution import Execution


router = APIRouter()
SETTINGS = get_settings()
song_division_service = SongDivisionService()
song_sentiment_analysis_service = SongSentimentAnalysisService()
song_emotion_analysis_service = SongEmotionAnalysisService()
image_to_base64_service = ImageToBase64Service()
image_description_service = ImageDescriptionService()
song_complete_analysis_service = SongCompleteAnalysisService()



@cache
def get_song_division_service():
    return song_division_service
@cache
def get_song_sentiment_analysis_service():
    return song_sentiment_analysis_service
@cache
def get_song_emotion_analysis_service():
    return song_emotion_analysis_service
@cache
def get_image_to_base64_service():
    return image_to_base64_service

@cache
def get_image_description_service():
    return image_description_service

@cache
def get_song_complete_analysis_service():
    return song_complete_analysis_service



@router.post("/analysis")
def complete_song_analysis(song:SongInput = Body(...),image:UploadFile = File(...),song_division = Depends(get_song_division_service), song_sentiment_analysis = Depends(get_song_sentiment_analysis_service), song_emotion_anaysis = Depends(get_song_emotion_analysis_service), image_to_base64 = Depends(get_image_to_base64_service), image_description = Depends(get_image_description_service), song_complete_analysis = Depends(get_song_complete_analysis_service), db_session = Depends(get_session)) -> SongFullAnalysisOutput:
    start = time.time()
    song_structure_output = song_division.divide_song_into_sections(song.lyrics)
    sentiment_output = song_sentiment_analysis.predict(song_structure_output)
    emotion_output = song_emotion_anaysis.predict(song_structure_output)
    base64 = image_to_base64.convert_to_base64(image)
    image_description_output = image_description.get_image_description(base64)
    meaning_output = song_complete_analysis.predict(song.name, song.artist, song_structure_output, sentiment_output, emotion_output, image_description_output)
    execution = Execution(time_in_seconds=time.time() - start, models_used=SETTINGS.models_names, lyrics_char_length=len(song.lyrics), version_number=SETTINGS.revision)
    output = SongFullAnalysisOutput(
        name=song.name,
        artist=song.artist,
        sentiment=sentiment_output,
        emotion=emotion_output,
        meaning=meaning_output,
        image_description=image_description_output,
        execution=execution,
    )
    profile = SongAnalysisProfile(
        song_title=song.name,
        artist_name=song.artist,
        sentiment=sentiment_output.dict(),
        emotion=emotion_output.dict(),
        meaning=meaning_output.dict(),
        image_description=image_description_output,
    )
    db_session.add(profile)
    db_session.commit()
    db_session.refresh(profile)
    end = time.time()
    
    
    return output