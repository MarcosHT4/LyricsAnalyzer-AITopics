from pydantic import BaseModel
from src.schemas.song_section_meaning_output import SongSectionMeaningOutput

class SongMeaningOutput(BaseModel):
    sections: list[SongSectionMeaningOutput]