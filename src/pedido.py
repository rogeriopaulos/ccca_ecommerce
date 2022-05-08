import datetime

from src.cupom import Cupom
from src.frete import Frete
from src.item import Item
from src.pedidoitem import PedidoItem
from src.validators import CPFValidator


class Pedido:

    def __init__(self, cpf: str, date: str = datetime.datetime.now().strftime("%d/%m/%Y")):
        self.cpf = CPFValidator(cpf)
        self.pedidos = []

        self.cupom: Cupom = None
        self.date = date
        self.frete = Frete()

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
            total = self.cupom.aplicar_desconto(total, self.date)
        total += self.frete.calcular_total()
        return total
