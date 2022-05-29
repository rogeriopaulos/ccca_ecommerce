from abc import ABC, abstractmethod

from src.dominio.entidade.pedido import Pedido


class PedidoRepositorio(ABC):

    @abstractmethod
    async def save(self, pedido: Pedido):
        ...

    @abstractmethod
    async def contagem(self) -> int:
        ...

    @abstractmethod
    async def all(self):
        ...

    @abstractmethod
    async def get(self, codigo_do_pedido):
        ...

    @abstractmethod
    async def clear(self):
        ...
