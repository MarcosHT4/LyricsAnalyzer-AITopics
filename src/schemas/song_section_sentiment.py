from pydantic import BaseModel
from src.schemas.sentiment_score_output import SentimentScoreOutput
class SongSectionSentiment(BaseModel):
    section:str
    scores: list[SentimentScoreOutput]