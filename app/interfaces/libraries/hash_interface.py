from abc import ABCMeta, abstractmethod


class HashInterface(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def generate_hash(key: str) -> str:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def verify_hash(key: str, _hash: str) -> bool:
        raise NotImplementedError
