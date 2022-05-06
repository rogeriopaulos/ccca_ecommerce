import pytest

from ccca_ecommerce.pedido import Pedido
from ccca_ecommerce.item import Item
from ccca_ecommerce.cupom import Cupom


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
    pedido = Pedido(cpf="007.997.733-28")
    pedido.adicionar_item(Item(id=1, descricao="Guitarra", preco=1000), 1)
    pedido.adicionar_item(Item(id=2, descricao="Amplificador", preco=5000), 1)
    pedido.adicionar_item(Item(id=3, descricao="Cabo", preco=30), 3)
    pedido.adicionar_cupom(Cupom(codigo="VALE20", percentual=20))
    total = pedido.calcular_total()
    assert total == 4872
