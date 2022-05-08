import datetime

from src.cupom import Cupom
from src.item import Item
from src.pedidoitem import PedidoItem
from src.validators import CPFValidator


class Pedido:

    def __init__(self, cpf: str, date: str = datetime.datetime.now().strftime("%d/%m/%Y")):
        self.cpf = CPFValidator(cpf)
        self.pedidos = []
        self.cupom = None

        self.date = date
        self.frete = 0

    def adicionar_item(self, item: Item, quantidade: float):
        self.pedidos.append(PedidoItem(id_item=item.id, preco=item.preco, quantidade=quantidade))

    def adicionar_cupom(self, cupom: Cupom):
        self.cupom = cupom

    def calcular_frete(self):
        return self.frete

    def calcular_total(self) -> float:
        total = sum([item.calcular_total() for item in self.pedidos])
        if self.cupom:
            total = self.cupom.aplicar_desconto(total, self.date)
        return total
