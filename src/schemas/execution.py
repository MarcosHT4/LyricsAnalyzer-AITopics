from pydantic import BaseModel

class Execution(BaseModel):
    time_in_seconds:float
    models_used:list[str]
    lyrics_char_length:int
    
    version_number:str