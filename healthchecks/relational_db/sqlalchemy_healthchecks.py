import sqlalchemy as sa


class ApplicationDataStore:
    def __init__(self):
        self.engine = sa.create_engine('postgresql://user:pass@localhost/mydb')
        self.conn = self.engine.connect()

    def is_healthy(self) -> bool:
        try:
            return self.conn.execute('SELECT 1').fetchone() == (1,)
        except IOError:
            return False
