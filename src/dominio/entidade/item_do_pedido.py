class ItemDoPedido:

    def __init__(self, id_item: int, preco: float, quantidade: int):
        self.id_item = id_item
        self.preco = preco
        if quantidade < 0:
            raise ValueError("Quantidade inválida")
        else:
            self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade
