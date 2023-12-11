import re
from src.schemas.song_structure import SongStructure
from src.schemas.song_section import SongSection
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

        return song_structure
        