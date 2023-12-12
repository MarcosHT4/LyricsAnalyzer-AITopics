from pydantic import BaseModel

class ScoreOutput(BaseModel):
    score:float
    label:str