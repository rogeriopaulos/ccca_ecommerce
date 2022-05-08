import pytest

from src.pedido import Pedido
from src.item import Item
from src.cupom import Cupom


def test_nao_deve_criar_pedido_com_cpf_invalido():
    with pytest.raises(ValueError, match="CPF Inválido"):
        Pedido(cpf="111.222.333-44")


def test_deve_criar_pedido_com_3_itens():
    pedido = Pedido(cpf="007.997.733-28")
    pedido.adicionar_item(Item(id=1, descricao="Guitarra", preco=1000), 1)
    pedido.adicionar_item(Item(id=2, descricao="Amplificador", preco=5000), 1)
    pedido.adicionar_item(Item(id=3, descricao="Cabo", preco=30), 3)
    total = pedido.calcular_total()
    assert total == 6090


def test_deve_criar_pedido_com_cupom_de_desconto():
    pedido = Pedido(cpf="007.997.733-28", date="08/05/2022")
    pedido.adicionar_item(Item(id=1, descricao="Guitarra", preco=1000), 1)
    pedido.adicionar_item(Item(id=2, descricao="Amplificador", preco=5000), 1)
    pedido.adicionar_item(Item(id=3, descricao="Cabo", preco=30), 3)
    pedido.adicionar_cupom(Cupom(codigo="VALE20", percentual=20, expiracao="08/05/2022"))
    total = pedido.calcular_total()
    assert total == 4872


def test_nao_deve_aplicar_cupom_de_desconto_expirado():
    with pytest.raises(ValueError, match="Cupom expirado"):
        pedido = Pedido(cpf="007.997.733-28")
        pedido.adicionar_item(Item(id=1, descricao="Guitarra", preco=1000), 1)
        pedido.adicionar_cupom(Cupom(codigo="VALE20", percentual=20, expiracao="01/01/2000"))
        pedido.calcular_total()


def test_deve_criar_pedido_com_3_itens_e_calcular_o_frete(self):
    pedido = Pedido(cpf="007.997.733-28")
    pedido.adicionar_item(
        Item(
            id=1,
            descricao="Guitarra",
            preco=1000,
            altura=100,
            largura=30,
            profundidade=10,
            peso=3
        ), 1
    )
    pedido.adicionar_item(
        Item(
            id=2,
            descricao="Amplificador",
            preco=5000,
            altura=50,
            largura=50,
            profundidade=50,
            peso=20
        ), 1
    )
    pedido.adicionar_item(
        Item(
            id=3,
            descricao="Cabo",
            preco=30,
            altura=10,
            largura=10,
            profundidade=10,
            peso=1
        ), 3
    )
    frete = pedido.calcular_frete()
    # total = pedido.calcular_total()
    assert frete == 260


# def test_pedido_com_valor_minimo_de_frete(self):
#     pedido = Pedido(cpf="007.997.733-28")
#     pedido.adicionar_item(Item(id=1, descricao="Guitarra", preco=1000), 1)
