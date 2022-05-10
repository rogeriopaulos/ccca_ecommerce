from fastapi import FastAPI

from src.http_api import Http


class FastApiAdapter(Http):

    def __init__(self):
        self.app = FastAPI()

    def on(self, method, url, callback):
        ...

    def listen(self, port):
        ...
