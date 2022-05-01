import pytest

from ccca_ecommerce.validators import CPFValidator


def test_deve_validar_um_cpf_valido():
    cpf_validator = CPFValidator(raw_cpf="962.844.320-89")
    assert cpf_validator.is_valid_cpf()


@pytest.mark.parametrize('cpf', ['111.111.111-11', '222.222.222-22', '333.333.333-33'])
def test_nao_deve_validar_um_cpf_invalido_com_todos_os_numeros_iguais(cpf):
    cpf_validator = CPFValidator(raw_cpf=cpf)
    assert not cpf_validator.is_valid_cpf()


def test_nao_deve_validar_um_cpf_invalido_que_seja_nulo():
    cpf_validator = CPFValidator()
    assert not cpf_validator.is_valid_cpf()


def test_deve_validar_um_cpf_valido_sem_pontos_e_tracos():
    cpf_validator = CPFValidator(raw_cpf="96284432089")
    assert cpf_validator.is_valid_cpf()


def test_extrair_digitos_verificadore():
    cpf_validator = CPFValidator(raw_cpf="962.844.320-89")
    clean_cpf = cpf_validator._clean_cpf()
    assert cpf_validator._extract_check_digits(clean_cpf) == "89"
