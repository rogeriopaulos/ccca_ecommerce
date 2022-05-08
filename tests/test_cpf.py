import pytest

from src.validators import CPFValidator


def test_deve_validar_um_cpf_valido():
    cpf = "962.844.320-89"
    cpf_validator = CPFValidator(raw_cpf=cpf)
    assert cpf_validator._is_valid_cpf(cpf)


@pytest.mark.parametrize('cpf', ['111.111.111-11', '222.222.222-22', '333.333.333-33'])
def test_nao_deve_validar_um_cpf_invalido_com_todos_os_numeros_iguais(cpf):
    with pytest.raises(ValueError, match="CPF Inválido"):
        CPFValidator(raw_cpf=cpf)


def test_nao_deve_validar_um_cpf_invalido_que_seja_nulo():
    with pytest.raises(ValueError, match="CPF Inválido"):
        CPFValidator()


def test_deve_validar_um_cpf_valido_sem_pontos_e_tracos():
    cpf = "96284432089"
    cpf_validator = CPFValidator(raw_cpf=cpf)
    assert cpf_validator._is_valid_cpf(cpf)


def test_extrair_digitos_verificadore():
    cpf = "962.844.320-89"
    cpf_validator = CPFValidator(raw_cpf=cpf)
    clean_cpf = cpf_validator._clean_cpf(cpf)
    assert cpf_validator._extract_check_digits(clean_cpf) == "89"
