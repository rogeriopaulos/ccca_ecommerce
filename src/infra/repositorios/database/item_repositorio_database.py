from src.dominio.entidade.item import Item
from src.dominio.repositorio.item_repositorio import ItemRepositorio
from src.infra.database.conexao import Conexao


class ItemRepositorioDatabase(ItemRepositorio):

    def __init__(self, conexao: Conexao):
        self.conexao = conexao

    async def get(self, id) -> Item:
        ...

    async def save(self, item: Item):
        ...

    async def all(self):
        itens_data = await self.conexao.query("SELECT * FROM ccca.item")
        return [
            Item(item[0].id, item[0].descricao, float(item[0].preco)) for item in itens_data
        ]