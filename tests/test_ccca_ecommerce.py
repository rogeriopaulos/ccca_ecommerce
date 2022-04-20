from ccca_ecommerce.core import Compra, Comprador, Pedido


def test_pedido_com_cpf_invalido_entao_compra_nao_finalizada():
    comprador = Comprador(nome="João Pereira", cpf="11122233344")
    pedido = Pedido(descricao="maçã", preco=1.99, quantidade=7)
    compra = Compra(comprador)
    compra.adicionar_pedido(pedido)
    assert not compra.finalizar_pedido()


def test_pedido_com_cpf_valido_entao_compra_finalizada():
    comprador = Comprador(nome="Rogério Paulo", cpf="00799773328")
    pedido = Pedido(descricao="banana", preco=0.99, quantidade=10)
    compra = Compra(comprador)
    compra.adicionar_pedido(pedido)
    assert compra.finalizar_pedido()


def test_pedido_com_3_itens():
    comprador = Comprador(nome="Rogério Paulo", cpf="00799773328")
    pedido1 = Pedido(descricao="banana", preco=0.99, quantidade=10)
    pedido2 = Pedido(descricao="macã", preco=2.50, quantidade=7)
    pedido3 = Pedido(descricao="melancia", preco=7.99, quantidade=2)
    compra = Compra(comprador)
    compra.adicionar_pedido(pedido1)
    compra.adicionar_pedido(pedido2)
    compra.adicionar_pedido(pedido3)
    assert compra.finalizar_pedido()
    assert len(compra.carrinho) == 3


def test_pedido_com_cupom_de_desconto():
    valor_do_cupom_de_desconto = 10
    comprador = Comprador(nome="Rogério Paulo", cpf="00799773328")
    pedido1 = Pedido(descricao="banana", preco=0.99, quantidade=10)
    pedido2 = Pedido(descricao="macã", preco=2.50, quantidade=7)
    pedido3 = Pedido(descricao="melancia", preco=7.99, quantidade=2)
    compra = Compra(comprador)
    compra.adicionar_pedido(pedido1)
    compra.adicionar_pedido(pedido2)
    compra.adicionar_pedido(pedido3)
    assert compra.valor_final(valor_do_cupom_de_desconto) == 33.379999999999995
