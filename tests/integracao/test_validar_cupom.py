import pytest
from src.aplicacao.validador_de_cupom import ValidadorDeCupom
from src.dominio.entidade.cupom import Cupom
from src.infra.repositorios.memoria.cupom_repositorio_memoria import \
    CupomRepositorioMemoria


@pytest.mark.asyncio
async def test_deve_validar_um_cupom_de_desconto_expirado():
    cupom_repo = CupomRepositorioMemoria()
    await cupom_repo.save(Cupom("VALE20", 20, "10/04/2022"))
    validador_de_cupom = ValidadorDeCupom(cupom_repo)

    input = {
        "codigo": "VALE20",
        "data": "10/05/2022"
    }
    output = await validador_de_cupom.executar(input)
    assert not output.get('cupom_nao_expirado')


@pytest.mark.asyncio
async def test_deve_validar_um_cupom_de_desconto_valido():
    cupom_repo = CupomRepositorioMemoria()
    await cupom_repo.save(Cupom("VALE20", 20, "10/06/2021"))
    validador_de_cupom = ValidadorDeCupom(cupom_repo)

    input = {
        "codigo": "VALE20",
        "data": "10/05/2021"
    }
    output = await validador_de_cupom.executar(input)
    assert output.get('cupom_nao_expirado')
