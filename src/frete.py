from src.item import Item


class Frete:
    def __init__(self):
        self._total = 0
        self._DISTANCE = 1000
        self._FACTOR = 100

    def adicionar_item(self, item: Item, quantidade: int):
        frete = item.calcular_volume() * self._DISTANCE * (item.calcular_densidade()/self._FACTOR)
        self._total += frete * quantidade

    def calcular_total(self):
        return 10 if self._total > 0 and self._total < 10 else self._total
