import pytest


# @pytest.mark.asyncio
@pytest.mark.skip(reason="Classe 'ObterPedidos' não implementada")
async def test_deve_obter_os_pedidos():
    pedidos = ObterPedidos()
    output = await pedidos.executar()
    assert len(output) == 0
