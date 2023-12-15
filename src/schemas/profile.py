from pydantic import BaseModel
from src.schemas.song_section_output import SongSectionOutput
class Profile(BaseModel):
    songs: list[str]
    sentiment:SongSectionOutput
    emotion:SongSectionOutput