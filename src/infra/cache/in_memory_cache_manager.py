from src.application.interfaces import CacheManager

class InMemoryCacheManager(CacheManager):
    memory: dict

    def __init__(self):
        self.memory = {}

    def get(self, key: str) -> str:
        return self.memory[key]

    def save(self, key: str, value: str) -> None:
        self.memory[key] = value
