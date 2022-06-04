import pytest
from src.dominio.entidade.item import Item


def test_lancar_uma_exception_se_o_peso_for_negativo():
    with pytest.raises(ValueError, match="Somente valores positivos são aceitos"):
        Item(id=1, descricao="Guitarra", preco=1000, peso=-3)
