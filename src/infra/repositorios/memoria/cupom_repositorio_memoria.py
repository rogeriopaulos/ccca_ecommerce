from src.dominio.entidade.cupom import Cupom
from src.dominio.repositorio.cupom_repositorio import CupomRepositorio


class CupomRepositorioMemoria(CupomRepositorio):

    def __init__(self):
        self.cupons = []

    async def get(self, codigo) -> Cupom:
        try:
            cupom = next(cupom for cupom in self.cupons if cupom.codigo == codigo)
        except StopIteration:
            raise ValueError("Cupom não encontrado")
        return cupom

    async def save(self, cupom: Cupom):
        self.cupons.append(cupom)

    async def all(self):
        return self.cupons
