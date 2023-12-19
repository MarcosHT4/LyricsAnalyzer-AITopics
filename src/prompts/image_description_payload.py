def get_image_description_payload(image:str) -> dict:
    return {
        "messages":[
        {
            "content": "Act as an album cover description specialist.",
            "role":"system"

        },    
        {
            "content": f"Describe the following image with the most possible accuracy. Make sure to emphazise the sentiment and emotions that are given by the image <img src=\"{image.decode('utf-8')}\"/>",
            "role":"user"
        },
        {
        "labels": {
            "creativity": 4,
            "helpfulness": 6,
            "humor": 0,
            "quality": 6
            },
        "role": "assistant"
        }
    ],
    "temperature": 0.5,
    "top_p": 0.7,
    "max_tokens": 512,
    "stream": False   
    }