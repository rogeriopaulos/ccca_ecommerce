class Item:

    def __init__(
        self, id: str,
        descricao: str,
        preco: float,
        altura: float,
        largura: float,
        profundidade: float,
        peso: float
    ):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade
        self.peso = peso
