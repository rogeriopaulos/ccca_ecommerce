from src.dominio.entidade.pedido import Pedido
from src.dominio.repositorio.cupom_repositorio import CupomRepositorio
from src.dominio.repositorio.item_repositorio import ItemRepositorio
from src.dominio.repositorio.pedido_repositorio import PedidoRepositorio


class FazerPedido:

    def __init__(
        self,
        item_repositorio: ItemRepositorio,
        pedido_repositorio: PedidoRepositorio,
        cupom_repositorio: CupomRepositorio
    ):
        self.item_repositorio = item_repositorio
        self.pedido_repositorio = pedido_repositorio
        self.cupom_repositorio = cupom_repositorio

    async def executar(self, input: dict) -> dict:
        sequencia = await self.pedido_repositorio.contagem() + 1
        pedido = Pedido(cpf=input.get("cpf"), data=input.get("data", None), sequencia=sequencia)
        for item_input in input.get("itens_do_pedido"):
            item = await self.item_repositorio.get(item_input.get("id"))
            pedido.adicionar_item(item, item_input.get("quantidade"))
        if input.get("cupom"):
            cupom = await self.cupom_repositorio.get(input.get('cupom'))
            pedido.adicionar_cupom(cupom)
        await self.pedido_repositorio.save(pedido)
        return {
            "total": pedido.calcular_total(),
            "codigo_do_pedido": pedido.codigo_do_pedido.valor
        }
