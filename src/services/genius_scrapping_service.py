import httpx
from fastapi import HTTPException
from bs4 import BeautifulSoup
import re
from src.schemas.song_input import SongInput
class GeniusScrappingService:
    async def get_song_from_genius(self, song_url:str, client:httpx.AsyncClient) -> SongInput:
        req = client.build_request("GET", song_url)
        try:
            response = await client.send(req)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Malformed URL")
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Song not found")
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        for br in soup.find_all("br"):
            br.replace_with("\n")
        title_element = soup.find("h1",{"class":re.compile(".*SongHeaderdesktop.*")})  
        artist_element = soup.find('a', {"class":re.compile(".*HeaderArtistAndTracklistdesktop.*")})  
        artist = artist_element.get_text()
        title = title_element.get_text()
        text_elements = soup.findAll('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
        text = [elem.get_text() for elem in text_elements]
        lyrics = '\n'.join(text)
        song = SongInput(name = title, artist = artist, lyrics = lyrics)
        
        return song
        