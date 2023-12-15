from pydantic import BaseModel, model_validator
from typing import Optional
from fastapi import UploadFile, File
import json

class SongInput(BaseModel):
    name:str
    artist:str
    lyrics:str
    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value