from abc import ABC, abstractmethod
from src.dominio.entidade.item import Item


class ItemRepositorio(ABC):

    @abstractmethod
    async def get(self, id: int) -> Item:
        ...

    @abstractmethod
    async def save(self):
        ...

    @abstractmethod
    async def all(self):
        ...
