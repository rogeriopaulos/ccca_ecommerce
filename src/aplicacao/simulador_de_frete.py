from src.dominio.repositorio.item_repositorio import ItemRepositorio
from src.dominio.entidade.frete import Frete


class SimuladorDeFrete:

    def __init__(self, item_repositorio: ItemRepositorio):
        self.item_repositorio = item_repositorio

    async def executar(self, input):
        frete = Frete()
        for item_pedido in input.get('itens_do_pedido'):
            item = await self.item_repositorio.get(item_pedido.get('id'))
            frete.adicionar_item(item, item_pedido.get('quantidade'))
        return {
            "total": frete.calcular_total()
        }
