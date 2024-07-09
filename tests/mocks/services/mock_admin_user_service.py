from typing import Optional, Tuple, List

from sqlalchemy_model_faker import factory

from app.interfaces.services.admin_user_service_interface import \
    AdminUserServiceInterface
from app.models.admin_user import AdminUser
from tests.mocks.model_factories.admin_user import admin_user_factory


class MockAdminUserService(AdminUserServiceInterface):

    @staticmethod
    def generate_admin_user(_id: Optional[str] = None) -> AdminUser:
        fields = {}
        if _id is not None:
            fields["id"] = _id
        return factory(AdminUser).make(fields)

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

    def count_admin_users(self) -> int:
        return 1

    def get_admin_users(self, offset: int = 0, limit: int = 20) -> List[AdminUser]:
        model_01 = self.generate_admin_user()
        model_02 = self.generate_admin_user()

        return [model_01, model_02]

    def delete_admin_user(self, admin_user_id: str) -> bool:
        return True

