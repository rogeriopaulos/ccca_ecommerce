from fastapi import FastAPI

from src.infra.repositorios.database.item_repositorio_database import ItemRepositorioDatabase
from src.infra.database.pg_conexao_adapter import PgConexaoAdapter
from src.aplicacao.obter_itens import ObterItens

app = FastAPI()


@app.get("/itens")
async def obter_itens():
    conn = PgConexaoAdapter()
    item_repo_db = ItemRepositorioDatabase(conn)
    await item_repo_db.all()
    obter_itens = ObterItens(item_repo_db)
    output = await obter_itens.executar()
    return output
