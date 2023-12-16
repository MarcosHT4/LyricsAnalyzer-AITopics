from pydantic import BaseModel
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.song_meaning_output import SongMeaningOutput
from typing import Optional

class SongFullAnalysisOutput(BaseModel):
    name: str
    artist: str
    sentiment: Optional[SongSectionOutput] = None
    emotion: Optional[SongSectionOutput] = None
    meaning: Optional[SongMeaningOutput] = None
    image_description: Optional[str] = None
