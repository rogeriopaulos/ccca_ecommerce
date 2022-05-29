from src.dominio.entidade.pedido import Pedido
from src.dominio.repositorio.pedido_repositorio import PedidoRepositorio


class PedidoRepositorioMemoria(PedidoRepositorio):

    def __init__(self):
        self.pedidos = []

    async def save(self, pedido: Pedido):
        self.pedidos.append(pedido)

    async def contagem(self):
        return len(self.pedidos)

    async def all(self):
        return self.pedidos

    async def get(self, codigo_do_pedido):
        ...

    async def clear(self):
        return await super().clear()
