from abc import ABCMeta, abstractmethod
from typing import List, Optional, Tuple

from ...models.admin_user import AdminUser


class AdminUserServiceInterface(metaclass=ABCMeta):

    @abstractmethod
    def sign_in(self, email: str,
                password: str) -> Tuple[Optional[AdminUser], Optional[str]]:
        raise NotImplementedError

    @abstractmethod
    def generate_access_token(self, admin_user_id: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_admin_user_by_token(self,
                                access_token: str) -> Optional[AdminUser]:
        raise NotImplementedError

    @abstractmethod
    def count_admin_users(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_admin_users(self,
                        offset: int = 0,
                        limit: int = 20) -> List[AdminUser]:
        raise NotImplementedError

    @abstractmethod
    def get_admin_user_by_id(self, admin_user_id: str) -> Optional[AdminUser]:
        raise NotImplementedError

    @abstractmethod
    def update_admin_user(self, admin_user_id: str,
                          admin: dict) -> Optional[AdminUser]:
        raise NotImplementedError

    @abstractmethod
    def delete_admin_user(self, admin_user_id: str) -> bool:
        raise NotImplementedError
