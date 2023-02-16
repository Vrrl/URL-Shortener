from abc import ABC, abstractmethod


class GetLinkUseCase:
    @abstractmethod
    def handle(self, key: str) -> str:
        raise NotImplementedError()
