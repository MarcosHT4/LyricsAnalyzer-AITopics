from pydantic import BaseModel
from src.config import get_settings

SETTINGS = get_settings()

class Status(BaseModel):
    api_status:str = "OK"
    api_name:str = SETTINGS.api_name
    version:str = SETTINGS.revision
    models_names:list[str] = SETTINGS.models_names