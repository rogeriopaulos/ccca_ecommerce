class Dimensao:

    def __init__(self, altura: float, largura: float, profundidade: float):
        if altura < 0 or largura < 0 or profundidade < 0:
            raise ValueError("Somente valores positivos são aceitos")
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

    @property
    def volume(self):
        return (self.largura/100) * (self.altura/100) * (self.profundidade/100)
