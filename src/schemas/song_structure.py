from pydantic import BaseModel
from src.schemas.song_section import SongSection
class SongStructure(BaseModel):
    sections:list[SongSection]