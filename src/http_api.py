from abc import ABC, abstractmethod


class Http(ABC):

    @abstractmethod
    def on(self, method: str, url: str, callback):
        ...

    @abstractmethod
    def listen(self, port: int):
        ...
