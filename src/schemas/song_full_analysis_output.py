from pydantic import BaseModel
from src.schemas.song_section_output import SongSectionOutput
from src.schemas.song_meaning_output import SongMeaningOutput

class SongFullAnalysisOutput(BaseModel):
    name: str
    artist: str
    sentiment: SongSectionOutput
    emotion: SongSectionOutput
    meaning: SongMeaningOutput
    image_description: str
