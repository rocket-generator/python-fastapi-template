from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class BaseRepositoryInterface(metaclass=ABCMeta):

    @property
    @abstractmethod
    def model(self):
        raise NotImplementedError

    @abstractmethod
    def list(self, offset: int = 0, limit: int = 20) -> [model]:
        raise NotImplementedError

    @abstractmethod
    def list_by_filter(self, offset: int = 0, limit: int = 20) -> [model]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, _id: str) -> model:
        raise NotImplementedError

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> model:
        raise NotImplementedError

    @abstractmethod
    def update(self, _id: str, data: Dict[str, Any]) -> model:
        raise NotImplementedError

    @abstractmethod
    def delete(self, _id: str) -> None:
        raise NotImplementedError
