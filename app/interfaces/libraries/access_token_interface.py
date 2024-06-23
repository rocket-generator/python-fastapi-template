from abc import ABCMeta, abstractmethod
from datetime import timedelta
from typing import Optional


class AccessTokenInterface(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_access_token(data: dict,
                            expires_delta: timedelta | None = None):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def extract_from_token(token: str) -> Optional[dict]:
        raise NotImplementedError
