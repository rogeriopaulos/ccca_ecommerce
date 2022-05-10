import datetime


class CodigoDoPedido:

    def __init__(self, data: str, sequencia: int):
        self.valor = self._gerar_codigo(data, sequencia)

    def _gerar_codigo(self, data, sequencia):
        ano = datetime.datetime.strptime(data, "%d/%m/%Y").year
        return f'{ano}{str(sequencia).zfill(8)}'
