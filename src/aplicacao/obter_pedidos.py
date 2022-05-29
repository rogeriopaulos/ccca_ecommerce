from src.dominio.repositorio.pedido_repositorio import PedidoRepositorio


class ObterPedidos:

    def __init__(self, pedido_repositorio: PedidoRepositorio):
        self.pedido_repositorio = pedido_repositorio

    async def executar(self):
        pedidos = await self.pedido_repositorio.all()
        return [
            {
                "codigo_do_pedido": pedido.codigo_do_pedido,
                "total": pedido.calcular_total(),
            }
            for pedido in pedidos
        ]
