from src.dominio.entidade.dimensao import Dimensao


def test_deve_criar_as_dimensoes():
    dimensao = Dimensao(altura=100, largura=30, profundidade=10)
    volume = dimensao.volume
    assert volume == 0.03
