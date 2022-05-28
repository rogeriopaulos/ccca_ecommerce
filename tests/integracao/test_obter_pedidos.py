import pytest


@pytest.mark.asyncio
async def test_deve_obter_os_pedidos():
    pedidos = ObterPedidos()
    output = await pedidos.executar()
    assert len(output) == 0
