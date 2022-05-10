from abc import ABC, abstractmethod
from src.dominio.entidade.cupom import Cupom


class CupomRepositorio(ABC):

    @abstractmethod
    async def get(self, codigo: str) -> Cupom:
        ...

    @abstractmethod
    async def save(self):
        ...

    @abstractmethod
    async def all(self):
        ...
