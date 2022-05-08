from src.dimensao import Dimensao
from src.frete import Frete
from src.item import Item


def test_deve_calcular_o_frete():
    frete = Frete()
    frete.adicionar_item(
        Item(
            id=1,
            descricao="Guitarra",
            preco=1000,
            dimensao=Dimensao(altura=100, largura=30, profundidade=10),
            peso=3
        ), 1
    )
    frete.adicionar_item(
        Item(
            id=2,
            descricao="Amplificador",
            preco=5000,
            dimensao=Dimensao(altura=50, largura=50, profundidade=50),
            peso=20
        ), 1
    )
    frete.adicionar_item(
        Item(
            id=3,
            descricao="Cabo",
            preco=30,
            dimensao=Dimensao(altura=10, largura=10, profundidade=10),
            peso=1
        ), 3
    )
    total = frete.calcular_total()
    assert total == 260


def test_deve_calcular_o_frete_com_preco_minimo():
    frete = Frete()
    frete.adicionar_item(
        Item(
            id=3,
            descricao="Cabo",
            preco=30,
            dimensao=Dimensao(altura=10, largura=10, profundidade=10),
            peso=0.9
        ), 1
    )
    total = frete.calcular_total()
    assert total == 10
