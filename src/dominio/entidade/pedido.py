import datetime

from src.dominio.entidade.codigo_do_pedido import CodigoDoPedido
from src.dominio.entidade.cupom import Cupom
from src.dominio.entidade.frete import Frete
from src.dominio.entidade.item import Item
from src.dominio.entidade.pedidoitem import PedidoItem
from src.dominio.entidade.validators import CPFValidator


class Pedido:

    def __init__(self, cpf: str, data: str = datetime.datetime.now().strftime("%d/%m/%Y"), sequencia: int = 1):
        self.cpf = CPFValidator(cpf)
        self.pedidos = []

        self.cupom: Cupom = None
        self.data = data
        self.frete = Frete()
        self.codigo_do_pedido: CodigoDoPedido = CodigoDoPedido(self.data, sequencia)

    def adicionar_item(self, item: Item, quantidade: float):
        self.frete.adicionar_item(item, quantidade)
        self.pedidos.append(PedidoItem(id_item=item.id, preco=item.preco, quantidade=quantidade))

    def adicionar_cupom(self, cupom: Cupom):
        self.cupom = cupom

    def calcular_frete(self):
        return self.frete.calcular_total()

    def calcular_total(self) -> float:
        total = sum([item.calcular_total() for item in self.pedidos])
        if self.cupom:
            total = self.cupom.aplicar_desconto(total, self.data)
        total += self.frete.calcular_total()
        return total
