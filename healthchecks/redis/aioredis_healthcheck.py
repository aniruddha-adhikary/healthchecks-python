import aioredis


class RedisCache:
    def __init__(self):
        self.redis = aioredis.ConnectionsPool('redis://localhost/1',
                                              minsize=1, maxsize=3)

    async def is_healthy(self) -> bool:
        """
        Redis has a Ping command. If we receive a Pong back, it
        means that Redis is healthy.
        """
        try:
            return await self.redis.execute(b'PING') == b'PONG'
        except IOError:
            return False
