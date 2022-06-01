import pytest
from src.aplicacao.fazer_pedido import FazerPedido
from src.aplicacao.obter_pedidos import ObterPedidos
from src.dominio.entidade.dimensao import Dimensao
from src.dominio.entidade.item import Item
from src.infra.database.pg_conexao_adapter import PgConexaoAdapter
from src.infra.repositorios.database.pedido_repositorio_database import \
    PedidoRepositorioDatabase
from src.infra.repositorios.memoria.cupom_repositorio_memoria import \
    CupomRepositorioMemoria
from src.infra.repositorios.memoria.item_repositorio_memoria import \
    ItemRepositorioMemoria


@pytest.fixture
def db_connection():
    return PgConexaoAdapter()


@pytest.fixture
@pytest.mark.asyncio
async def pedido_repo_db(db_connection):
    pedido_repo_db = PedidoRepositorioDatabase(db_connection)
    yield pedido_repo_db
    await pedido_repo_db.clear()
    await db_connection.close()


@pytest.mark.asyncio
async def test_deve_obter_uma_lista_vazia_de_pedidos(pedido_repo_db):
    pedidos = ObterPedidos(pedido_repo_db)
    output = await pedidos.executar()
    assert len(output) == 0


@pytest.mark.asyncio
async def test_deve_obter_os_pedidos_cadastrados(pedido_repo_db):
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(100, 50, 10), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    cupom_repo = CupomRepositorioMemoria()
    fazer_pedido = FazerPedido(item_repo, pedido_repo_db, cupom_repo)
    input = {
        "cpf": "007.997.733-28",
        "itens_do_pedido": [
            {"id": 1, "quantidade": 1},
            {"id": 2, "quantidade": 1},
            {"id": 3, "quantidade": 3},
        ],
        "data": "10/05/2021"
    }
    await fazer_pedido.executar(input)
    pedidos = ObterPedidos(pedido_repo_db)
    output = await pedidos.executar()
    assert len(output) == 1
    assert output[0]['codigo_do_pedido'] == '202100000001'
    # assert output[0]['total'] == 6350
    assert output[0]['total'] == 6370.0
