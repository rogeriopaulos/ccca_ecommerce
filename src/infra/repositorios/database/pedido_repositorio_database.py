from src.dominio.entidade.pedido import Pedido
from src.dominio.repositorio.pedido_repositorio import PedidoRepositorio
from src.infra.database.conexao import Conexao


class PedidoRepositorioDatabase(PedidoRepositorio):

    def __init__(self, conexao: Conexao):
        self.conexao = conexao

    async def save(self, pedido):
        insert_into = "code, cpf, issue_date, freight, sequence, total"
        values_dados_do_pedido = f"""{pedido.codigo_do_pedido.valor}, '{pedido.cpf.cpf}', '{pedido.data}',
        {pedido.frete.calcular_total()}, {pedido.sequencia}, {pedido.calcular_total()}"""
        codigo_do_cupom = pedido.cupom.codigo if pedido.cupom else None
        if codigo_do_cupom:
            insert_into + ', coupon_code'
            values_dados_do_pedido + f', {codigo_do_cupom}'
        query = f"INSERT INTO ccca.order ({insert_into}) VALUES ({values_dados_do_pedido}) RETURNING *"
        dados_do_pedido = await self.conexao.query(query)
        for item in pedido.pedidos:
            insert_into_item = 'ccca.order_item (id_order, id_item, price, quantity)'
            values_item = f'{dados_do_pedido[0][0]}, {item.id_item}, {item.preco}, {item.quantidade}'
            await self.conexao.query(f"INSERT INTO {insert_into_item} VALUES ({values_item})")

    async def contagem(self):
        row = await self.conexao.query("SELECT count(*)::int FROM ccca.order")
        return row[0][0]

    async def all(self):
        pedidos_fromdb = await self.conexao.query("SELECT code FROM ccca.order")
        pedidos = []
        for pedido in pedidos_fromdb:
            pedido_obj = await self.get(pedido[0])
            pedidos.append(pedido_obj)
        return pedidos

    async def get(self, codigo_do_pedido):
        pedido_fromdb = await self.conexao.query(
            f"SELECT cpf, issue_date, sequence FROM ccca.order WHERE code = '{codigo_do_pedido}'"
        )
        data = pedido_fromdb[0][1].strftime("%d/%m/%Y")
        return Pedido(cpf=pedido_fromdb[0][0], data=data, sequencia=pedido_fromdb[0][2])

    async def clear(self):
        await self.conexao.query('DELETE FROM ccca.order_item')
        await self.conexao.query('DELETE FROM ccca.order')
