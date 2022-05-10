import psycopg2

from src.infra.database.conexao import Conexao


class PgConexaoAdapter(Conexao):

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="debugdb",
            user="test",
            password="psql01",
            port="5432"
        )

    async def query(self, statement: str, params=None):
        cur = self.conn.cursor()
        cur.execute(statement)
        result = cur.fetchall()
        cur.close()
        return result
