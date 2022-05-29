import pytest
from src.aplicacao.obter_pedidos import ObterPedidos
from src.infra.database.pg_conexao_adapter import PgConexaoAdapter
from src.infra.repositorios.database.pedido_repositorio_database import \
    PedidoRepositorioDatabase


@pytest.mark.asyncio
async def test_deve_obter_os_pedidos():
    conn = PgConexaoAdapter()
    pedido_repo = PedidoRepositorioDatabase(conn)
    pedidos = ObterPedidos(pedido_repo)
    output = await pedidos.executar()
    assert len(output) == 0
