from fastapi import Depends

from src.application.interfaces import GetLinkUseCase, CacheManager
from src.infra.cache import RedisCacheManager, InMemoryCacheManager

class GetLinkService(GetLinkUseCase):

    cache_manager: CacheManager

    def __init__(self, cache_manager: CacheManager = Depends(RedisCacheManager)):
        self.cache_manager = cache_manager

    def handle(self, key: str) -> str:
        link = self.cache_manager.get(key)
        return link