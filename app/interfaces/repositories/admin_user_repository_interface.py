from abc import ABCMeta, abstractmethod

from ...models.admin_user import AdminUser


class AdminUserRepositoryInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_by_email(self, email: str) -> AdminUser | None:
        raise NotImplementedError
