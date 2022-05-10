from src.dominio.repositorio.item_repositorio import ItemRepositorio


class ObterItens:

    def __init__(self, item_repositorio: ItemRepositorio):
        self.item_repositorio = item_repositorio

    async def executar(self):
        itens = await self.item_repositorio.all()
        return [
            {
                "id": item.id,
                "descricao": item.descricao,
                "preco": item.preco
            }
            for item in itens
        ]
