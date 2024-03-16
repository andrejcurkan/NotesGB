from abc import ABC, abstractmethod

class NoteStorage(ABC):
    @abstractmethod
    def create(self, title: str, content: str) -> None:
        pass

    @abstractmethod
    def read_all(self) -> list:
        pass

    @abstractmethod
    def read(self, title: str) -> str:
        pass

    @abstractmethod
    def update(self, title: str, content: str) -> bool:
        pass

    @abstractmethod
    def delete(self, title: str) -> bool:
        pass
