from fastapi import FastAPI

from src.infra.http.http_api import Http


class FastApiAdapter(Http):

    def __init__(self):
        self.app = FastAPI()

    def on(self, method: str, url: str, callback):
        ...

    def listen(self, port: int):
        ...
