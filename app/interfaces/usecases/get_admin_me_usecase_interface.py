from abc import ABCMeta, abstractmethod
from typing import Optional, Tuple

from ...models.admin_user import AdminUser


class GetAdminMeUsecaseInterface(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, admin_user_id: str) -> Optional[AdminUser]:
        raise NotImplementedError
