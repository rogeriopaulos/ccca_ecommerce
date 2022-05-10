from fastapi import FastAPI

from src.item_repositorio_memoria import ItemRepositorioMemoria
from src.item import Item
from src.dimensao import Dimensao
from src.obter_itens import ObterItens

app = FastAPI()


@app.get("/itens")
async def obter_itens():
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(100, 30, 10), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    obter_itens = ObterItens(item_repo)
    output = await obter_itens.executar()
    return output
