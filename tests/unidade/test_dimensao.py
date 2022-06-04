import pytest
from src.dominio.entidade.dimensao import Dimensao


def test_deve_criar_as_dimensoes():
    dimensao = Dimensao(altura=100, largura=30, profundidade=10)
    volume = dimensao.volume
    assert volume == 0.03


def test_lancar_uma_exception_se_alguma_dimensao_for_negativa():
    with pytest.raises(ValueError, match="Somente valores positivos são aceitos"):
        Dimensao(altura=-100, largura=30, profundidade=10)
        Dimensao(altura=100, largura=-30, profundidade=10)
        Dimensao(altura=100, largura=30, profundidade=-10)
