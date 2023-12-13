from langchain.output_parsers import PydanticOutputParser
from src.schemas.song_meaning_output import SongMeaningOutput
def get_song_meaning_parser():
    return PydanticOutputParser(pydantic_object=SongMeaningOutput)
