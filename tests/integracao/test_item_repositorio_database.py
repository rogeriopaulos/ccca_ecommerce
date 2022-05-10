import pytest
from src.infra.database.pg_conexao_adapter import PgConexaoAdapter
from src.infra.repositorios.database.item_repositorio_database import \
    ItemRepositorioDatabase


@pytest.mark.skip(reason="BD não foi alimentado")
async def test_deve_retornar_itens_do_bd():
    conn = PgConexaoAdapter()
    item_repo_db = ItemRepositorioDatabase(conn)
    itens = await item_repo_db.all()
    assert len(itens) == 3
