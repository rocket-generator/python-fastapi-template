from typing import Optional, Type

from app.interfaces.repositories.admin_user_repository_interface import \
    AdminUserRepositoryInterface
from app.models.admin_user import AdminUser
from tests.mocks.model_factories.admin_user import admin_user_factory
from tests.mocks.repositories.mock_base_repository import MockBaseRepository


class MockAdminUserRepository(AdminUserRepositoryInterface,
                              MockBaseRepository):

    @property
    def model(self):
        return AdminUser

    def generate_model(self,
                       _id: Optional[str] = None,
                       data: Optional[dict] = None) -> AdminUser:
        return admin_user_factory(_id=_id, data=data)

    def get_by_email(self, email: str) -> AdminUser | None:
        return self.generate_model(data={"email": email})

