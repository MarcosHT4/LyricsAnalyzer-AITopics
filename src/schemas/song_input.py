from pydantic import BaseModel

class SongInput(BaseModel):
    name:str
    artist:str
    lyrics:str