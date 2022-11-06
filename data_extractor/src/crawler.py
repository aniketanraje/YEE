import requests

class Crawler:
    def __init__(self, url):
        self.url = url 
        self.response = requests.get(self.url)
