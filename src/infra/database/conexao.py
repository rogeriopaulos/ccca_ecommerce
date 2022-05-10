from abc import ABC, abstractmethod


class Conexao(ABC):

    @abstractmethod
    async def query(self, params):
        ...
