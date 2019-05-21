from yapsy.IPlugin import IPlugin
from urllib.request import urlopen
import json
import os


class NASAPlugin(IPlugin):
    def process(self, msg, client):
        if "!space" in msg["text"]:
            response = urlopen(
                f'https://api.nasa.gov/planetary/apod?api_key={os.getenv("NASA_API_KEY")}'
            )
            js = json.load(response)
            response = f"{js['title']} {js['url']}"
            client.send_message(response)
