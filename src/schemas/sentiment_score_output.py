from pydantic import BaseModel

class SentimentScoreOutput(BaseModel):
    score:float
    label:str