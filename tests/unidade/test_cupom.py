import pytest

from src.dominio.entidade.cupom import Cupom


def test_aplicar_desconto():
    cupom = Cupom(codigo="VALE20", percentual=20, expiracao="08/05/2022")
    valor = 1000
    valor_com_desconto = cupom.aplicar_desconto(valor, "07/05/2022")
    assert valor_com_desconto == 800


def test_deve_criar_um_cupom_expirado():
    cupom = Cupom(codigo="VALE20", percentual=20, expiracao="01/01/2000")
    assert not cupom.cupom_nao_expirado(today="08/05/2022")


def test_cupom_com_data_no_formato_invalido_nao_deve_ser_aplicado():
    with pytest.raises(ValueError, match="Informe uma data no formato dd/mm/aaaa"):
        cupom = Cupom(codigo="VALE20", percentual=20, expiracao="2022-05-08")
        cupom.cupom_nao_expirado(today="2022-05-08")
