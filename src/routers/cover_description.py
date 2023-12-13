from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File
)
import time
from functools import cache
from src.config import get_settings
from src.services.image_to_base64_service import ImageToBase64Service
from src.services.image_description_service import ImageDescriptionService


router = APIRouter()
SETTINGS = get_settings()
image_to_base64_service = ImageToBase64Service()
image_description_service = ImageDescriptionService()


@cache
def get_image_to_base64_service():
    return image_to_base64_service

@cache
def get_image_description_service():
    return image_description_service



@router.post("/cover-description")
def analyze_cover(file:UploadFile = File(...), creativity:float = 0.5,image_to_base64 = Depends(get_image_to_base64_service), image_description = Depends(get_image_description_service)) -> str:
    start = time.time()
    base64 = image_to_base64.convert_to_base64(file)
    image_description_output = image_description.get_image_description(base64, creativity)
    return image_description_output

