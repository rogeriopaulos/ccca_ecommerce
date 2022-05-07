import datetime


class Cupom:

    def __init__(self, codigo: str, percentual: float, expiracao: str):
        self.codigo = codigo
        self.percentual = percentual
        self.expiracao = expiracao

        self._today = datetime.datetime.now().date()

    def cupom_nao_expirado(self):
        try:
            data_expiracao = datetime.datetime.strptime(self.expiracao, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Informe uma data no formato dd/mm/aaaa")
        return self._today <= data_expiracao

    def aplicar_cupom(self, total):
        if self.cupom_nao_expirado():
            return total - ((total * self.percentual) / 100)
        else:
            raise ValueError("Cupom expirado")
