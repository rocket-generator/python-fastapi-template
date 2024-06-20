from typing import Optional, Tuple

from app.interfaces.services.admin_user_service_interface import AdminUserServiceInterface
from app.models.admin_user import AdminUser
from sqlalchemy_model_faker import factory


class MockAdminUserService(AdminUserServiceInterface):

    @staticmethod
    def generate_admin_user(_id: Optional[str] = None, email: Optional[str] = None) -> AdminUser:
        fields = {}
        if _id is not None:
            fields["id"] = _id
        if email is not None:
            fields["email"] = email
        return factory(AdminUser).make(fields)

    def sign_in(self, email: str,
                password: str) -> Tuple[Optional[AdminUser], Optional[str]]:

        return self.generate_admin_user(email=email), "jwt"

    def generate_access_token(self, admin_user_id: str) -> str:

        return "jwt"

    def get_admin_user_by_token(self,
                                access_token: str) -> Optional[AdminUser]:
        return factory(AdminUser).make()

    def get_admin_user_by_id(self, admin_user_id: str) -> Optional[AdminUser]:
        return self.generate_admin_user(_id=admin_user_id)

    def update_admin_user(self, admin_user_id: str,
                          data: dict) -> Optional[AdminUser]:
        email = None
        if "email" in data:
            email = data["email"]
        return self.generate_admin_user(_id=admin_user_id, email=email)
