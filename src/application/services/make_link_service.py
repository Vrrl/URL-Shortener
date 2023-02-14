import random
import string
from fastapi import Depends

from src.application.interfaces import MakeLinkUseCase, CacheManager
from src.infra.cache import RedisCacheManager, InMemoryCacheManager

class MakeLinkService(MakeLinkUseCase):

    cache_manager: CacheManager

    def __init__(self, cache_manager: CacheManager = Depends(RedisCacheManager)):
        self.cache_manager = cache_manager

    def handle(self, url: str) -> str:
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

        self.cache_manager.save(key, url)

        return key