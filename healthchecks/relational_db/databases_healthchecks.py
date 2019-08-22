from databases import Database


class ApplicationDataStore:
    def __init__(self):
        self.database = Database('postgresql://user:pass@localhost/mydb')

    async def is_healthy(self) -> bool:
        try:
            await self.database.fetch_one('SELECT 1')
            return True
        except IOError:
            return False
