from src.pedido import Pedido
from src.pedido_repositorio import PedidoRepositorio


class PedidoRepositorioMemoria(PedidoRepositorio):

    def __init__(self):
        self.pedidos = []

    async def save(self, pedido: Pedido):
        self.pedidos.append(pedido)
