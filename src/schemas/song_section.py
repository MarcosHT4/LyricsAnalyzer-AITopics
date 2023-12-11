from pydantic import BaseModel

class SongSection(BaseModel):
    section:str
    lyrics:str
    