from fastapi import Depends

from src.application.interfaces import MakeLinkUseCase, CacheManager
from src.infra.cache import RedisCacheManager, InMemoryCacheManager
from src.domain.entities import Link

class MakeLinkService(MakeLinkUseCase):

    cache_manager: CacheManager

    def __init__(self, cache_manager: CacheManager = Depends(RedisCacheManager)):
        self.cache_manager = cache_manager

    def handle(self, url: str) -> Link:
        new_link = Link(url=url)
        new_link.generate_key()
        
        self.cache_manager.save(new_link.key, new_link.url)

        return new_link