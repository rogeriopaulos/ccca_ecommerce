from src.dominio.entidade.item import Item


class CalculadoraDeFrete:

    def __init__(self):
        self._total = 0
        self._DISTANCIA = 1000
        self._FATOR = 100
        self._FRETE_MINIMO = 10

    def calcular(self, item: Item, quantidade: int):
        frete = item.calcular_volume() * self._DISTANCIA * (item.calcular_densidade()/self._FATOR)
        return frete * quantidade
