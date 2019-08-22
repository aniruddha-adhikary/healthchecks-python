import psycopg2


class ApplicationDataStore:
    def __init__(self):
        self.connection = psycopg2.connect('dbname=test user=postgres')
        self.cursor = self.connection.cursor()

    def is_healthy(self) -> bool:
        try:
            self.cursor.execute('SELECT 1')
            return self.cursor.fetchone() == (1,)
        except IOError:
            return False
