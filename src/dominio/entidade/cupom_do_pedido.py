class CupomDoPedido:

    def __init__(self, codigo, percentual):
        self.codigo = codigo
        self.percentual = percentual

    def aplicar_desconto(self, total):
        return float(total) - ((float(total) * float(self.percentual)) / 100.0)
