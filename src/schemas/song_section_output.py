from pydantic import BaseModel
from src.schemas.score_output import ScoreOutput
class SongSectionOutput(BaseModel):
    section:str
    scores: list[ScoreOutput]