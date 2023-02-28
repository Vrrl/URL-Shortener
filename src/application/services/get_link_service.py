from fastapi import Depends

from src.application.interfaces import GetLinkUseCase, CacheManager
from src.infra.cache import RedisCacheManager, InMemoryCacheManager
from src.domain.entities import Link


class GetLinkService(GetLinkUseCase):
    cache_manager: CacheManager

    def __init__(self, cache_manager: CacheManager = Depends(InMemoryCacheManager)):
        self.cache_manager = cache_manager

    def handle(self, key: str) -> Link:
        url = self.cache_manager.get(key)

        return url
