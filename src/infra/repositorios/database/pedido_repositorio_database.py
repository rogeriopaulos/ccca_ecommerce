from src.dominio.repositorio.pedido_repositorio import PedidoRepositorio
from src.infra.database.conexao import Conexao


class PedidoRepositorioDatabase(PedidoRepositorio):

    def __init__(self, conexao: Conexao):
        self.conexao = conexao

    async def save(self, pedido):
        dados_do_pedido = await self.conexao.query(
            f"""INSERT INTO ccca.order (code, cpf, issue_date, freight, sequence, total, cupom)
            VALUES ({pedido.codigo_do_pedido}, {pedido.cpf}, {pedido.data}, {pedido.frete.calcular_total()},
            {pedido.sequencia}, {pedido.calcular_total()}, {pedido.cupom})
            RETURNING *"""
        )
        for item in dados_do_pedido:
            await self.conexao.query(
                f"""INSERT INTO ccca.order_item (id_order, id_item, price, quantity)
                VALUES {dados_do_pedido.id, item.id, item.preco, item.quantidade}"""
            )

    async def contagem(self):
        row = await self.conexao.query("SELECT count(*)::int FROM ccca.order")
        return row.count
