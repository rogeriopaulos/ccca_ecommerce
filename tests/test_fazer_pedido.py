import pytest

from src.item import Item
from src.dimensao import Dimensao
from src.fazer_pedido import FazerPedido
from src.item_repositorio_memoria import ItemRepositorioMemoria
from src.pedido_repositorio_memoria import PedidoRepositorioMemoria


@pytest.mark.asyncio
async def test_deve_fazer_um_pedido():
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(100, 30, 10), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    pedido_repo = PedidoRepositorioMemoria()
    fazer_pedido = FazerPedido(item_repo, pedido_repo)
    input = {
        "cpf": "007.997.733-28",
        "itens_do_pedido": [
            {"id": 1, "quantidade": 1},
            {"id": 2, "quantidade": 1},
            {"id": 3, "quantidade": 3},
        ]
    }
    output = await fazer_pedido.executar(input)
    assert output.get("total") == 6350
