import pytest
import requests


@pytest.mark.asyncio
async def test_deve_chamar_itens():
    response = requests.get("http://localhost:8000/itens")
    itens = response.json()
    assert len(itens) == 3
