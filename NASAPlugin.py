from yapsy.IPlugin import IPlugin
from urllib.request import urlopen
import json
import os
import random
import io

class NASAPlugin(IPlugin):
    def process(self, msg, client):
        if "!space" in msg["text"]:
            response = urlopen(
                f'https://api.nasa.gov/planetary/apod?api_key={os.getenv("NASA_API_KEY")}'
            )
            js = json.load(response)
            response = f"{js['title']} {js['url']}"
            client.send_message(response)
        if "!dscover" in msg["text"].lower():
            response = urlopen(
                f'https://api.nasa.gov/EPIC/api/natural/images?api_key={os.getenv("NASA_API_KEY")}'
            )
            js = random.choice(json.load(response))
            image = urlopen(f"https://epic.gsfc.nasa.gov/archive/natural/{js['date'][0:4]}/{js['date'][5:7]}/{js['date'][8:10]}/jpg/{js['image']}.jpg")
            data = io.BytesIO(image.read())
            image_url = client.upload_image(data, "image/jpeg")
            client.send_message_with_image(image_url, js['caption'])
