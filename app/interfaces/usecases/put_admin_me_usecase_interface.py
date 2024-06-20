from abc import ABCMeta, abstractmethod
from typing import Optional, Tuple

from ...models.admin_user import AdminUser


class PutAdminMeUsecaseInterface(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, user_id: str, data: dict) -> Optional[AdminUser]:
        raise NotImplementedError
