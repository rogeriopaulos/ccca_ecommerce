import psycopg2
import psycopg2.extras

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
        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(statement)
        try:
            result = cur.fetchall()
        except psycopg2.ProgrammingError:
            result = None
        self.conn.commit()
        cur.close()
        return result

    async def close(self):
        self.conn.close()
