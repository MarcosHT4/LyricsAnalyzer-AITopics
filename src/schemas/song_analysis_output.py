from pydantic import BaseModel
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.song_meaning_output import SongMeaningOutput
from typing import Optional
from src.schemas.execution import Execution

class SongAnalysisOutput(BaseModel):
    name: str
    artist: str
    execution: Execution
    analysis: Optional[SongSectionOutput] = None
    meaning: Optional[SongMeaningOutput] = None
