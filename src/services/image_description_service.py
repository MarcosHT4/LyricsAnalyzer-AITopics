from src.prompts.image_description_payload import get_image_description_payload
import requests
from fastapi import HTTPException 
from src.config import (
    get_settings,
    get_secret_settings
)

SETTINGS = get_settings()
SECRET_SETTINGS = get_secret_settings()
class ImageDescriptionService:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {SECRET_SETTINGS.nvidia_key}",
            "Accept": "application/json",
        }
        self.url = SETTINGS.models_versions[2][0]
        self.fetch_url_format = SETTINGS.models_versions[2][1]
        

    def get_image_description(self, img:str, creativity:float) -> str:
        session = requests.Session()
        json_payload = get_image_description_payload(img, creativity)
        response = session.post(self.url, headers=self.headers, json=json_payload)
        while response.status_code == 202:
            request_id = response.headers.get("NVCF-REQID")
            fetch_url = self.fetch_url_format + request_id
            response = session.get(fetch_url, headers=self.headers)
        try:    
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise HTTPException(status_code=413, detail="The image resolution is too high, please upload a smaller image")
        response_body = response.json()
        return response_body["choices"][0]["message"]["content"]
