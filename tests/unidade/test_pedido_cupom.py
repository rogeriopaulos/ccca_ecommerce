from src.dominio.entidade.cupom import Cupom
from src.dominio.entidade.cupom_do_pedido import CupomDoPedido


def test_aplicar_desconto():
    cupom = Cupom(codigo="VALE20", percentual=20, expiracao="08/05/2022")
    pedido_cupom = CupomDoPedido(cupom.codigo, cupom.percentual)
    valor = 1000
    valor_com_desconto = pedido_cupom.aplicar_desconto(valor)
    assert valor_com_desconto == 800
