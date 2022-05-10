from src.dominio.entidade.pedido import Pedido
from src.dominio.repositorio.pedido_repositorio import PedidoRepositorio


class PedidoRepositorioMemoria(PedidoRepositorio):

    def __init__(self):
        self.pedidos = []

    async def save(self, pedido: Pedido):
        self.pedidos.append(pedido)

    async def contagem(self):
        return len(self.pedidos)
