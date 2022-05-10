from abc import ABC, abstractmethod
from src.pedido import Pedido


class PedidoRepositorio(ABC):

    @abstractmethod
    async def save(self, pedido: Pedido):
        ...
