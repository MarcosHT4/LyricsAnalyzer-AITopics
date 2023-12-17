from pydantic import BaseModel
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.song_meaning_output import SongMeaningOutput
from typing import Optional
from src.schemas.execution import Execution

class SongFullAnalysisOutput(BaseModel):
    name: str
    artist: str
    sentiment: Optional[SongSectionOutput] = None
    emotion: Optional[SongSectionOutput] = None
    meaning: Optional[SongMeaningOutput] = None
    image_description: Optional[str] = None
    execution: Optional[Execution] = None
