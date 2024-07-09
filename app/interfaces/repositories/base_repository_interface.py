from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List


class BaseRepositoryInterface(metaclass=ABCMeta):

    @property
    @abstractmethod
    def model(self):
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def count_by_filter(self, _filter: dict) -> int:
        raise NotImplementedError

    @abstractmethod
    def list(self, offset: int = 0, limit: int = 20) -> List[model]:
        raise NotImplementedError

    @abstractmethod
    def list_by_filter(self,
                       _filter: dict,
                       offset: int = 0,
                       limit: int = 20) -> List[model]:
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
