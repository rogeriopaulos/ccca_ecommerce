import pytest
from src.dominio.entidade.item_do_pedido import ItemDoPedido


def test_deve_criar_um_item_de_pedido():
    item_do_pedido = ItemDoPedido(id_item=1, preco=1000.0, quantidade=2)
    assert item_do_pedido.calcular_total() == 2000.0


def test_deve_lancar_uma_exception_se_a_quantidade_for_negativa():
    with pytest.raises(ValueError, match="Quantidade inválida"):
        ItemDoPedido(id_item=1, preco=1000.0, quantidade=-2)
