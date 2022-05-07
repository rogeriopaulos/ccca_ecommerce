import datetime
import pytest

from ccca_ecommerce.cupom import Cupom


def test_cupom_com_data_no_formato_invalido_nao_deve_ser_aplicado():
    with pytest.raises(ValueError, match="Informe uma data no formato dd/mm/aaaa"):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        cupom = Cupom(codigo="VALE20", percentual=20, expiracao=today)
        cupom.cupom_nao_expirado()
