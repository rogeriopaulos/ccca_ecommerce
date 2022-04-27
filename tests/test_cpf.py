from ccca_ecommerce.core import Comprador


def test_deve_validar_um_cpf_valido():
    comprador = Comprador(nome="Rogério Paulo", cpf="007.997.733-28")
    assert comprador.is_valid_cpf()


def test_deve_validar_um_cpf_invalido_com_todos_os_numeros_iguais():
    comprador = Comprador(nome="Rogério Paulo", cpf="111.111.111-11")
    assert not comprador.is_valid_cpf()


def test_deve_validar_um_cpf_invalido_que_seja_nulo():
    comprador = Comprador(nome="Rogério Paulo", cpf=None)
    assert not comprador.is_valid_cpf()


def test_deve_validar_um_cpf_valido_sem_pontos_e_tracos():
    comprador = Comprador(nome="Rogério Paulo", cpf="00799773328")
    assert comprador.is_valid_cpf()
