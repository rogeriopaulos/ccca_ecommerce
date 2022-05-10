from src.dominio.entidade.codigo_do_pedido import CodigoDoPedido


def test_deve_gerar_o_codigo_do_pedido():
    codigo_do_pedido = CodigoDoPedido("10/05/2021", 1)
    assert codigo_do_pedido.valor == "202100000001"
