import re
from src.schemas.song_structure import SongStructure
from src.schemas.song_section import SongSection
from fastapi import HTTPException
class SongDivisionService:
    def divide_song_into_sections(self, song:str) -> SongStructure:
        
       
        section_pattern = re.compile(r'\[([^]]+)\](.*?)(?=\[(?:\1|.*?)\]|$)', re.DOTALL | re.IGNORECASE)


        sections = re.findall(section_pattern, song)
        result:list[SongSection] = []


        for section_name, section_content in sections:
            section_type = section_name.strip()
            section_content = section_content.strip()

            song_section = SongSection(section=section_type, lyrics=section_content)

            result.append(song_section)

        key_to_check = 'section'
        seen_values = set()

        for d in reversed(result):
            value = d.dict().get(key_to_check)
            if value in seen_values:
                result.remove(d)
            else:
                seen_values.add(value)    

        song_structure = SongStructure(sections=result)  

        if(song_structure.sections == []):
            raise HTTPException(status_code=422, detail="Incorrect format, the format should be [section_name] section_content for each section Example: [Verse 1] This is the first verse [Chorus] This is the chorus")
        return song_structure
        