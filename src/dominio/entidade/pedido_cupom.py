class PedidoCupom:

    def __init__(self, codigo, percentual):
        self.codigo = codigo
        self.percentual = percentual

    def aplicar_desconto(self, total, today):
        return total - ((total * self.percentual) / 100)
