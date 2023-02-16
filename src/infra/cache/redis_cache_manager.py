import redis

from src.application.interfaces import CacheManager


class RedisCacheManager(CacheManager):
    _client: redis.Redis

    def __init__(self):
        pool = redis.ConnectionPool(host="localhost", port=6379, db=0)
        self._client = redis.Redis(connection_pool=pool)

    def get(self, key: str) -> str:
        return self._client.get(str(key))

    def save(self, key: str, value: str) -> None:
        self._client.set(str(key), value)
