import pytest
from src.aplicacao.obter_itens import ObterItens
from src.dominio.entidade.dimensao import Dimensao
from src.dominio.entidade.item import Item
from src.infra.repositorios.memoria.item_repositorio_memoria import \
    ItemRepositorioMemoria


@pytest.mark.asyncio
async def test_deve_buscar_os_itens():
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(100, 30, 10), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    obter_itens = ObterItens(item_repo)
    output = await obter_itens.executar()
    assert len(output) == 3
