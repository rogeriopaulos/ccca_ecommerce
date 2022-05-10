from src.dominio.entidade.item import Item
from src.dominio.repositorio.item_repositorio import ItemRepositorio


class ItemRepositorioMemoria(ItemRepositorio):

    def __init__(self):
        self.itens = []

    async def get(self, id) -> Item:
        try:
            item = next(item for item in self.itens if item.id == id)
        except StopIteration:
            raise ValueError("Item não encontrado")
        return item

    async def save(self, item: Item):
        self.itens.append(item)

    async def all(self):
        return self.itens
