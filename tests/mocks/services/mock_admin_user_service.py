from typing import Optional, Tuple

from sqlalchemy_model_faker import factory

from app.interfaces.services.admin_user_service_interface import \
    AdminUserServiceInterface
from app.models.admin_user import AdminUser
from tests.mocks.model_factories.admin_user import admin_user_factory


class MockAdminUserService(AdminUserServiceInterface):

    def sign_in(self, email: str,
                password: str) -> Tuple[Optional[AdminUser], Optional[str]]:
        return admin_user_factory(data={"email": email}), "jwt"

    def generate_access_token(self, admin_user_id: str) -> str:
        return "jwt"

    def get_admin_user_by_token(self,
                                access_token: str) -> Optional[AdminUser]:
        return factory(AdminUser).make()

    def get_admin_user_by_id(self, admin_user_id: str) -> Optional[AdminUser]:
        return admin_user_factory(_id=admin_user_id)

    def update_admin_user(self, admin_user_id: str,
                          data: dict) -> Optional[AdminUser]:
        email = None
        if "email" in data:
            email = data["email"]
        return admin_user_factory(_id=admin_user_id, data={"email": email})
