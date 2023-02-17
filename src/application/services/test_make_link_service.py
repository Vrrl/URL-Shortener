from fastapi import Depends

from src.application.interfaces import MakeLinkUseCase, CacheManager
from src.infra.cache import RedisCacheManager, InMemoryCacheManager
from src.domain.entities import Link
from .make_link_service import MakeLinkService


def test_make_link_service():
    data = {"url": "http://www.google.com"}
    in_memory_cache = InMemoryCacheManager()

    in_memory_cache.save("KEY_TEST", data["url"])

    SUT = MakeLinkService(in_memory_cache)

    res = SUT.handle(url=data["url"])

    assert res.key is not None
    assert res.url == data["url"]
    assert in_memory_cache.memory[res.key] == data["url"]
    # just to test
