import redis


class RedisCache:
    def __init__(self):
        self.redis = redis.StrictRedis.from_url('redis://localhost/1')

    def is_healthy(self) -> bool:
        """
        Redis has a Ping command. If we receive a Pong back, it
        means that Redis is healthy.
        """
        try:
            return self.redis.ping()
        except IOError:
            return False
