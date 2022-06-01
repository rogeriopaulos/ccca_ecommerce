import pytest
from src.aplicacao.simulador_de_frete import SimuladorDeFrete
from src.dominio.entidade.dimensao import Dimensao
from src.dominio.entidade.item import Item
from src.infra.repositorios.memoria.item_repositorio_memoria import \
    ItemRepositorioMemoria


@pytest.mark.asyncio
async def test_deve_simular_o_frete_do_pedido():
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(50, 100, 15), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    simulador_de_frete = SimuladorDeFrete(item_repo)
    input = {
        "itens_do_pedido": [
            {"id": 1, "quantidade": 1},
            {"id": 2, "quantidade": 1},
            {"id": 3, "quantidade": 3},
        ],
    }
    output = await simulador_de_frete.executar(input)
    assert output.get('total') == 260
