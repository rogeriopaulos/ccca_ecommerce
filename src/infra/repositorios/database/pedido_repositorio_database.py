# from src.dominio.entidade.cupom import Cupom
# from src.dominio.entidade.dimensao import Dimensao
# from src.dominio.entidade.item import Item
from src.dominio.entidade.cupom_do_pedido import CupomDoPedido
from src.dominio.entidade.item_do_pedido import ItemDoPedido
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
            insert_into = insert_into + ', coupon_code, coupon_percentage'
            values_dados_do_pedido = values_dados_do_pedido + f", '{codigo_do_cupom}', {pedido.cupom.percentual}"
        query = f"INSERT INTO ccca.order ({insert_into}) VALUES ({values_dados_do_pedido}) RETURNING *"
        dados_do_pedido = await self.conexao.query(query)
        for item in pedido.pedidos:
            insert_into_item = 'ccca.order_item (id_order, id_item, price, quantity)'
            values_item = f'{dados_do_pedido[0].get("id_order")}, {item.id_item}, {item.preco}, {item.quantidade}'
            await self.conexao.query(f"INSERT INTO {insert_into_item} VALUES ({values_item})")

    async def contagem(self):
        row = await self.conexao.query("SELECT count(*)::int FROM ccca.order")
        return row[0]['count']

    async def all(self):
        pedidos_fromdb = await self.conexao.query("SELECT code FROM ccca.order")
        pedidos = []
        for pedido in pedidos_fromdb:
            pedido_obj = await self.get(pedido.get('code'))
            pedidos.append(pedido_obj)
        return pedidos

    async def get(self, codigo_do_pedido):
        pedido_fromdb = await self.conexao.query(f"SELECT * FROM ccca.order WHERE code = '{codigo_do_pedido}'")
        pedido_fromdb = pedido_fromdb[0]
        data = pedido_fromdb.get('issue_date').strftime("%d/%m/%Y")
        pedido = Pedido(cpf=pedido_fromdb.get('cpf'), data=data, sequencia=pedido_fromdb.get('sequence'))
        id_order = pedido_fromdb.get('id_order')
        itens_do_pedido_fromdb = await self.conexao.query(f"SELECT * FROM ccca.order_item WHERE id_order = {id_order}")
        # alternativa 1 - hydrate
        pedido.pedidos = [
            ItemDoPedido(
                id_item=item.get('id_item'),
                preco=float(item.get('price')),
                quantidade=item.get('quantity')
            ) for item in itens_do_pedido_fromdb
        ]
        pedido.frete._total = float(pedido_fromdb.get('freight'))
        if pedido_fromdb.get('coupon_code'):
            pedido.cupom = CupomDoPedido(
                codigo=pedido_fromdb.get('coupon_code'),
                percentual=pedido_fromdb.get('coupon_percentage')
            )
        # alternativa 2
        # for item_do_pedido in itens_do_pedido_fromdb:
        #     item = await self.conexao.query(
        #         f"SELECT * FROM ccca.item WHERE id_item = {item_do_pedido.get('id_item')}"
        #     )
        #     item = item[0]
        #     item_obj = Item(
        #         id=item.get('id_item'),
        #         descricao=item.get('description'),
        #         preco=float(item.get('price')),
        #         dimensao=Dimensao(
        #             altura=float(item.get('height')),
        #             largura=float(item.get('width')),
        #             profundidade=float(item.get('length'))
        #         ),
        #         peso=item.get('weight')
        #     )
        #     pedido.adicionar_item(item_obj, item_do_pedido.get('quantity'))
        # if pedido_fromdb.get('coupon_code'):
        #     cupom_fromdb = await self.conexao.query(
        #         f"SELECT * FROM ccca.coupon WHERE code = '{pedido_fromdb.get('coupon_code')}'"
        #     )
        #     cupom_fromdb = cupom_fromdb[0]
        #     cupom = Cupom(
        #         codigo=cupom_fromdb.get('code'),
        #         percentual=cupom_fromdb.get('percentage'),
        #         expiracao=cupom_fromdb.get('expire_date').strftime("%d/%m/%Y")
        #     )
        #     pedido.adicionar_cupom(cupom)
        return pedido

    async def clear(self):
        await self.conexao.query('DELETE FROM ccca.order_item')
        await self.conexao.query('DELETE FROM ccca.order')
