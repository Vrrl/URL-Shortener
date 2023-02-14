from abc import ABC, abstractmethod


class CacheManager(ABC):

    @abstractmethod
    def get(self, key: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def save(self, key: str, value: str) -> None:
        raise NotImplementedError()
