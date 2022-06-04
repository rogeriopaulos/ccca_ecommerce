from src.dominio.repositorio.pedido_repositorio import PedidoRepositorio


class ObterPedido:

    def __init__(self, pedido_repositorio: PedidoRepositorio):
        self.pedido_repositorio = pedido_repositorio

    async def executar(self, code: str):
        pedido = await self.pedido_repositorio.get(code)
        return {
            "codigo_do_pedido": pedido.codigo_do_pedido.valor,
            "total": pedido.calcular_total(),
        }
