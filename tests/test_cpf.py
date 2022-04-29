import pytest

from ccca_ecommerce.core import Comprador


def test_deve_validar_um_cpf_valido():
    comprador = Comprador(nome="Fulano de Tal", cpf="007.997.733-28")
    assert comprador.is_valid_cpf()


@pytest.mark.parametrize('cpf', ['111.111.111-11', '222.222.222-22', '333.333.333-33'])
def test_deve_validar_um_cpf_invalido_com_todos_os_numeros_iguais(cpf):
    comprador = Comprador(nome="Fulano de Tal", cpf=cpf)
    assert not comprador.is_valid_cpf()


def test_deve_validar_um_cpf_invalido_que_seja_nulo():
    comprador = Comprador(nome="Fulano de Tal", cpf=None)
    assert not comprador.is_valid_cpf()


def test_deve_validar_um_cpf_valido_sem_pontos_e_tracos():
    comprador = Comprador(nome="Fulano de Tal", cpf="96284432089")
    assert comprador.is_valid_cpf()
