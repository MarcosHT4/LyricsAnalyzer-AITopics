from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache

class Settings(BaseSettings):
    api_name:str = "Lyrics Analyzer Services"
    revision:str = "0.0.1"
    models_names:list[str] = [
        "DistilBERT Base Uncased FineTuned SST-2 - HuggingFace",
        "Roberta Base GO Emotions - SamLowe",
        "NeVa-22B - NVIDIA",
        "GPT-4 - LangChain"
    ]
    models_versions:list = [
        "src/models/distilbert-base-uncased-finetuned-sst-2-english",
        "src/models/roberta-base-go_emotions",
        ["https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/8bf70738-59b9-4e5f-bc87-7ab4203be7a0",
         "https://api.nvcf.nvidia.com/v2/nvcf/pexec/status/"],
        "gpt-3.5-turbo-1106"]
    
class SecretSettings(BaseSettings):
    openai_key:str
    nvidia_key:str
    model_config = SettingsConfigDict(env_file=".env")    

@cache
def get_secret_settings():
    return SecretSettings()

@cache
def get_settings():
    return Settings()

 

