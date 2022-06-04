import datetime


class Cupom:

    def __init__(self, codigo: str, percentual: float, expiracao: str):
        self.codigo = codigo
        self.percentual = percentual
        self.expiracao = expiracao

    def cupom_nao_expirado(self, today):
        try:
            data_expiracao = datetime.datetime.strptime(self.expiracao, "%d/%m/%Y").date()
            today = datetime.datetime.strptime(today, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Informe uma data no formato dd/mm/aaaa")
        return today <= data_expiracao

    def aplicar_desconto(self, total):
        return float(total) - ((float(total) * float(self.percentual)) / 100.0)
