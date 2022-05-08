from src.dimensao import Dimensao


class Item:

    def __init__(self, id: str, descricao: str, preco: float, dimensao: Dimensao = None, peso: float = None):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.dimensao = dimensao
        self.peso = peso

    def calcular_volume(self):
        if self.dimensao:
            return self.dimensao.volume
        return 0

    def calcular_densidade(self):
        if self.dimensao and self.peso:
            return self.peso/self.calcular_volume()
        return 0
