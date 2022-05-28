import pytest
from src.aplicacao.fazer_pedido import FazerPedido
from src.dominio.entidade.cupom import Cupom
from src.dominio.entidade.dimensao import Dimensao
from src.dominio.entidade.item import Item
from src.infra.repositorios.database.pedido_repositorio_database import PedidoRepositorioDatabase
from src.infra.repositorios.memoria.cupom_repositorio_memoria import CupomRepositorioMemoria
from src.infra.repositorios.memoria.item_repositorio_memoria import ItemRepositorioMemoria
from src.infra.repositorios.memoria.pedido_repositorio_memoria import PedidoRepositorioMemoria
from src.infra.database.pg_conexao_adapter import PgConexaoAdapter


@pytest.mark.asyncio
async def test_deve_fazer_um_pedido():
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(100, 30, 10), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    # pedido_repo = PedidoRepositorioMemoria()
    conexao = PgConexaoAdapter()
    pedido_repo = PedidoRepositorioDatabase(conexao)
    cupom_repo = CupomRepositorioMemoria()
    fazer_pedido = FazerPedido(item_repo, pedido_repo, cupom_repo)
    input = {
        "cpf": "007.997.733-28",
        "itens_do_pedido": [
            {"id": 1, "quantidade": 1},
            {"id": 2, "quantidade": 1},
            {"id": 3, "quantidade": 3},
        ],
        "data": "10/05/2021"
    }
    output = await fazer_pedido.executar(input)
    assert output.get("total") == 6350


@pytest.mark.asyncio
async def test_deve_fazer_um_pedido_com_desconto():
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(100, 30, 10), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    pedido_repo = PedidoRepositorioMemoria()
    cupom_repo = CupomRepositorioMemoria()
    await cupom_repo.save(Cupom("VALE20", 20, "10/05/2022"))
    fazer_pedido = FazerPedido(item_repo, pedido_repo, cupom_repo)
    input = {
        "cpf": "007.997.733-28",
        "itens_do_pedido": [
            {"id": 1, "quantidade": 1},
            {"id": 2, "quantidade": 1},
            {"id": 3, "quantidade": 3},
        ],
        "data": "10/05/2022",
        "cupom": "VALE20"
    }
    output = await fazer_pedido.executar(input)
    assert output.get("total") == 5132


@pytest.mark.asyncio
async def test_deve_fazer_um_pedido_e_gerar_o_codigo_do_pedido():
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(100, 30, 10), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    pedido_repo = PedidoRepositorioMemoria()
    cupom_repo = CupomRepositorioMemoria()
    fazer_pedido = FazerPedido(item_repo, pedido_repo, cupom_repo)
    input = {
        "cpf": "007.997.733-28",
        "itens_do_pedido": [
            {"id": 1, "quantidade": 1},
            {"id": 2, "quantidade": 1},
            {"id": 3, "quantidade": 3},
        ],
        "data": "10/05/2021"
    }
    output = await fazer_pedido.executar(input)
    assert output.get('codigo_do_pedido') == '202100000001'
