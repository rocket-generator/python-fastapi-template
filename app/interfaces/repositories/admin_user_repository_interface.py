from abc import ABCMeta, abstractmethod

from ...models.admin_user import AdminUser
from .base_repository_interface import BaseRepositoryInterface


class AdminUserRepositoryInterface(BaseRepositoryInterface, metaclass=ABCMeta):

    @abstractmethod
    def get_by_email(self, email: str) -> AdminUser | None:
        raise NotImplementedError
