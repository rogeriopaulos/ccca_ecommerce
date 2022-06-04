class ItemDoPedido:

    def __init__(self, id_item: int, preco: float, quantidade: int):
        self.id_item = id_item
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade
