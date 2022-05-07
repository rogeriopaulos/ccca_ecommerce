from ccca_ecommerce.cupom import Cupom
from ccca_ecommerce.item import Item
from ccca_ecommerce.pedidoitem import PedidoItem
from ccca_ecommerce.validators import CPFValidator


class Pedido:

    def __init__(self, cpf):
        self.cpf = CPFValidator(cpf)
        self.pedidos = []
        self.cupom = None

    def adicionar_item(self, item: Item, quantidade: float):
        self.pedidos.append(PedidoItem(id_item=item.id, preco=item.preco, quantidade=quantidade))

    def adicionar_cupom(self, cupom: Cupom):
        self.cupom = cupom

    def calcular_total(self):
        total = sum([item.calcular_total() for item in self.pedidos])
        if self.cupom:
            total = self.cupom.aplicar_cupom(total)
        return total
