from abc import ABC, abstractmethod


class MakeLinkUseCase:

    @abstractmethod
    def handle(self, url: str) -> str:
        raise NotImplementedError()
