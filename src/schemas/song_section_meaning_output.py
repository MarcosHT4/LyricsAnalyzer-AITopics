from pydantic import BaseModel, Field

class SongSectionMeaningOutput(BaseModel):
    section:str
    meaning:str