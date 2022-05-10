import pytest

from src.dominio.entidade.dimensao import Dimensao
from src.dominio.entidade.pedido import Pedido
from src.dominio.entidade.item import Item
from src.dominio.entidade.cupom import Cupom


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
    pedido = Pedido(cpf="007.997.733-28", data="08/05/2022")
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


def test_deve_criar_pedido_com_3_itens_e_calcular_o_frete():
    pedido = Pedido(cpf="007.997.733-28")
    pedido.adicionar_item(
        Item(
            id=1,
            descricao="Guitarra",
            preco=1000,
            dimensao=Dimensao(altura=100, largura=30, profundidade=10),
            peso=3
        ), 1
    )
    pedido.adicionar_item(
        Item(
            id=2,
            descricao="Amplificador",
            preco=5000,
            dimensao=Dimensao(altura=50, largura=50, profundidade=50),
            peso=20
        ), 1
    )
    pedido.adicionar_item(
        Item(
            id=3,
            descricao="Cabo",
            preco=30,
            dimensao=Dimensao(altura=10, largura=10, profundidade=10),
            peso=1
        ), 3
    )
    frete = pedido.calcular_frete()
    total = pedido.calcular_total()
    assert frete == 260
    assert total == 6350


def test_deve_criar_pedido_e_gerar_um_codigo_no_padrao_AAAAPPPPPPPP():
    pedido = Pedido(cpf="007.997.733-28", data="10/05/2021")
    assert pedido.codigo_do_pedido.valor == "202100000001"
