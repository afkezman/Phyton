import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent"

def encode_image_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

def predict_with_gemini(image_path):
    image_base64 = encode_image_base64(image_path)
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",  # atau image/png
                            "data": image_base64
                        }
                    },
                    {
                        "text": "Analisa gambar ini: apakah ini luka diabetes ringan, sedang, atau parah? Jelaskan alasannya juga secara singkat."
                    }
                ]
            }
        ]
    }

    response = requests.post(
        f"{ENDPOINT}?key={API_KEY}",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        result = response.json()
        message = result['candidates'][0]['content']['parts'][0]['text']
        return message
    else:
        print("Error:", response.status_code, response.text)
        return "Terjadi kesalahan dalam memproses gambar."
