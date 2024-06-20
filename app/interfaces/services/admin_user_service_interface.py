from abc import ABCMeta, abstractmethod
from typing import Optional, Tuple

from ...models.admin_user import AdminUser


class AdminUserServiceInterface(metaclass=ABCMeta):

    @abstractmethod
    def sign_in(self, email: str,
                password: str) -> Tuple[Optional[AdminUser], Optional[str]]:
        raise NotImplementedError

    @abstractmethod
    def generate_access_token(self, user_id: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_admin_user_by_token(self,
                                access_token: str) -> Optional[AdminUser]:
        raise NotImplementedError
