from src.item import Item


class Frete:
    def __init__(self):
        self._total = 0
        self._DISTANCIA = 1000
        self._FATOR = 100
        self._FRETE_MINIMO = 10

    def adicionar_item(self, item: Item, quantidade: int):
        frete = item.calcular_volume() * self._DISTANCIA * (item.calcular_densidade()/self._FATOR)
        self._total += frete * quantidade

    def calcular_total(self):
        return self._FRETE_MINIMO if self._total > 0 and self._total < self._FRETE_MINIMO else self._total
