from src.dominio.entidade.cupom import Cupom
from src.dominio.entidade.pedido_cupom import PedidoCupom


def test_aplicar_desconto():
    cupom = Cupom(codigo="VALE20", percentual=20, expiracao="08/05/2022")
    pedido_cupom = PedidoCupom(cupom.codigo, cupom.percentual)
    valor = 1000
    valor_com_desconto = pedido_cupom.aplicar_desconto(valor, "07/05/2022")
    assert valor_com_desconto == 800
