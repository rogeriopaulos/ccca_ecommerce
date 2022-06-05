from fastapi import FastAPI

from src.infra.repositorios.database.item_repositorio_database import ItemRepositorioDatabase
from src.infra.repositorios.database.pedido_repositorio_database import PedidoRepositorioDatabase
from src.infra.database.pg_conexao_adapter import PgConexaoAdapter
from src.aplicacao.obter_itens import ObterItens
from src.aplicacao.obter_pedidos import ObterPedidos
from src.aplicacao.obter_pedido import ObterPedido


app = FastAPI()


@app.get("/itens")
async def obter_itens():
    conn = PgConexaoAdapter()
    item_repo_db = ItemRepositorioDatabase(conn)
    await item_repo_db.all()
    obter_itens = ObterItens(item_repo_db)
    output = await obter_itens.executar()
    return output


@app.get("/pedidos")
async def obter_pedidos():
    conn = PgConexaoAdapter()
    pedido_repo_db = PedidoRepositorioDatabase(conn)
    await pedido_repo_db.all()
    pedidos = ObterPedidos(pedido_repo_db)
    output = await pedidos.executar()
    return output


@app.get("/pedidos/{code}")
async def obter_pedido(code):
    conn = PgConexaoAdapter()
    pedido_repo_db = PedidoRepositorioDatabase(conn)
    await pedido_repo_db.all()
    pedido = ObterPedido(pedido_repo_db)
    output = await pedido.executar(code)
    return output
