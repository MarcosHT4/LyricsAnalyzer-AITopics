from pydantic import BaseModel
class SongSectionMeaningOutput(BaseModel):
    section:str
    meaning:str    