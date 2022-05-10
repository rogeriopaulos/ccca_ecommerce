from src.pedido import Pedido
from src.item_repositorio import ItemRepositorio
from src.pedido_repositorio import PedidoRepositorio


class FazerPedido:

    def __init__(self, item_repositorio: ItemRepositorio, pedido_repositorio: PedidoRepositorio):
        self.item_repositorio = item_repositorio
        self.pedido_repositorio = pedido_repositorio

    async def executar(self, input: dict) -> float:
        pedido = Pedido(cpf=input.get("cpf"))
        for item_input in input.get("itens_do_pedido"):
            item = await self.item_repositorio.get(item_input.get("id"))
            pedido.adicionar_item(item, item_input.get("quantidade"))
        await self.pedido_repositorio.save(pedido)
        total = pedido.calcular_total()
        return {
            "total": total
        }
