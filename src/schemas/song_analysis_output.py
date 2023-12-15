from pydantic import BaseModel
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.song_meaning_output import SongMeaningOutput
from typing import Optional

class SongAnalysisOutput(BaseModel):
    name: str
    artist: str
    analysis: Optional[SongSectionOutput] = None
    meaning: Optional[SongMeaningOutput] = None
