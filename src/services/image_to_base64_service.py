from fastapi import (
    UploadFile,
    HTTPException
)
from PIL import (
    Image,
    UnidentifiedImageError
)
import io
import base64
class ImageToBase64Service:
    def convert_to_base64(self,image:UploadFile) -> str:
        img_stream = io.BytesIO(image.file.read())
        try:
            img = Image.open(img_stream)
        except UnidentifiedImageError:
            raise HTTPException(status_code=415, detail="Invalid image file")
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        img_base64 = bytes("data:image/jpeg;base64,", encoding='utf-8') + img_str
        return img_base64