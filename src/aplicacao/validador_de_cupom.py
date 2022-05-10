from src.dominio.repositorio.cupom_repositorio import CupomRepositorio


class ValidadorDeCupom():

    def __init__(self, cupom_repositorio: CupomRepositorio):
        self.cupom_repositorio = cupom_repositorio

    async def executar(self, input: dict) -> dict:
        cupom = await self.cupom_repositorio.get(input.get("codigo"))
        cupom_nao_expirado = cupom.cupom_nao_expirado(input.get("data"))
        return {
            "cupom_nao_expirado": cupom_nao_expirado
        }
