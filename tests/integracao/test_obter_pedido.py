import pytest
import pytest_asyncio
from src.aplicacao.fazer_pedido import FazerPedido
from src.aplicacao.obter_pedido import ObterPedido
from src.dominio.entidade.cupom import Cupom
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


@pytest_asyncio.fixture
async def pedido_repo_db(db_connection):
    pedido_repo_db = PedidoRepositorioDatabase(db_connection)
    yield pedido_repo_db
    await pedido_repo_db.clear()
    await db_connection.close()


@pytest.mark.asyncio
async def test_deve_obter_um_pedido_pelo_codigo(pedido_repo_db):
    item_repo = ItemRepositorioMemoria()
    await item_repo.save(Item(1, "Guitarra", 1000, Dimensao(100, 50, 10), 3))
    await item_repo.save(Item(2, "Amplificador", 5000, Dimensao(50, 50, 50), 20))
    await item_repo.save(Item(3, "Cabo", 30, Dimensao(10, 10, 10), 1))
    cupom_repo = CupomRepositorioMemoria()
    await cupom_repo.save(Cupom("VALE20", 20, "10/03/2021"))
    fazer_pedido = FazerPedido(item_repo, pedido_repo_db, cupom_repo)
    input = {
        "cpf": "007.997.733-28",
        "itens_do_pedido": [
            {"id": 1, "quantidade": 1},
            {"id": 2, "quantidade": 1},
            {"id": 3, "quantidade": 3},
        ],
        "data": "01/03/2021",
        "cupom": "VALE20"
    }
    await fazer_pedido.executar(input)
    pedido = ObterPedido(pedido_repo_db)
    output = await pedido.executar('202100000001')
    assert output.get('codigo_do_pedido') == '202100000001'
    assert output.get('total') == 5132
